# -*- coding: utf-8 -*-
"""Guardian. En modo 'observacion' solo mira y reporta. En 'reparar' actua sobre lo declarado."""
from __future__ import annotations

import json
import shutil
import sqlite3
import sys
import time
from pathlib import Path

import config
import eventos
import heartbeat
import incidencias
import llm
import memoria
from util import ahora, atomic_write_json, bloqueo, edad_segundos

LOCK = config.SISTEMA / ".guardian.lock"
INFORME = config.SISTEMA / "guardian.json"


def _c_lmstudio() -> dict:
    try:
        modelos = llm.modelos()
        if modelos:
            return {"estado": "ok", "detalle": f"{len(modelos)} modelos disponibles"}
        return {"estado": "error", "detalle": "servidor arriba pero sin modelos",
                "incidencia": ("lmstudio", "sin modelos cargados", "media")}
    except llm.ErrorLLM as e:
        return {"estado": "error", "detalle": str(e)[:200],
                "incidencia": ("lmstudio", "servidor caido", "alta")}


def _c_sqlite() -> dict:
    if not memoria.DB_PATH.exists():
        return {"estado": "aviso", "detalle": "sin indice todavia"}
    mb = memoria.DB_PATH.stat().st_size / 1e6
    salida = {"estado": "ok", "detalle": f"{mb:.1f} MB"}
    marca = config.SISTEMA / ".integridad"
    if edad_segundos(marca) > int(config.get("guardian.verificar_integridad_min", 60)) * 60:
        try:
            conn = sqlite3.connect(memoria.DB_PATH, timeout=20)
            res = conn.execute("PRAGMA integrity_check").fetchone()
            conn.close()
            if (res[0] if res else "") != "ok":
                salida = {"estado": "error", "detalle": f"integridad: {res[0]}",
                          "incidencia": ("sqlite", "indice corrupto", "critica")}
        except sqlite3.Error as e:
            salida = {"estado": "error", "detalle": str(e)[:200],
                      "incidencia": ("sqlite", "no se pudo abrir", "alta")}
        marca.write_text(ahora(), encoding="utf-8")
    return salida


def _c_indice() -> dict:
    try:
        conn = memoria.connect()
        filas = conn.execute("SELECT COUNT(*) c FROM files").fetchone()["c"]
        chunks = conn.execute("SELECT COUNT(*) c FROM chunks").fetchone()["c"]
        conn.close()
    except sqlite3.Error as e:
        return {"estado": "error", "detalle": str(e)[:200],
                "incidencia": ("indice", "no consultable", "alta")}
    if filas == 0:
        return {"estado": "aviso", "detalle": "indice vacio"}
    return {"estado": "ok", "detalle": f"{filas} archivos / {chunks} fragmentos"}


def _c_heartbeat() -> dict:
    seg = heartbeat.segundos_sin_latir()
    if heartbeat.activo():
        return {"estado": "ok", "detalle": f"activo, paso {heartbeat.leer().get('paso')}"}
    if seg > int(config.get("guardian.heartbeat_vencido_seg", 300)):
        return {"estado": "aviso", "detalle": f"sin latido desde hace {int(seg)}s"}
    return {"estado": "ok", "detalle": "parado (normal)"}


def _c_incidencias() -> dict:
    r = incidencias.resumen()
    criticas = r["por_gravedad"].get("critica", 0) + r["por_gravedad"].get("alta", 0)
    if criticas >= 3:
        return {"estado": "error", "detalle": f"{criticas} incidencias graves abiertas"}
    if r["total"]:
        return {"estado": "aviso", "detalle": f"{r['total']} abiertas"}
    return {"estado": "ok", "detalle": "ninguna"}


def _c_locks() -> dict:
    raros = []
    for ruta in (memoria.LOCK_PATH, LOCK):
        if ruta.exists() and edad_segundos(ruta) > memoria.LOCK_STALE_SECONDS:
            raros.append(ruta.name)
    return {"estado": "aviso" if raros else "ok", "detalle": ", ".join(raros) or "limpios"}


def _c_logs() -> dict:
    total = 0
    grandes = []
    for ruta in list((config.VAULT / ".memoria").glob("*.log")):
        if ruta.exists():
            mb = ruta.stat().st_size / 1e6
            total += mb
            if mb > float(config.get("guardian.log_max_mb", 5)):
                grandes.append(f"{ruta.name} ({mb:.1f} MB)")
    return {"estado": "aviso" if grandes else "ok",
            "detalle": ", ".join(grandes) or f"{total:.1f} MB en total"}


def _c_deps() -> dict:
    req = Path(__file__).resolve().parent / "requirements.txt"
    if not req.exists():
        return {"estado": "ok", "detalle": "sin requirements.txt"}
    faltan = []
    for linea in req.read_text(encoding="utf-8").splitlines():
        linea = linea.split("#")[0].strip()
        if not linea:
            continue
        nombre = linea.split("=")[0].split(">")[0].split("<")[0].strip()
        try:
            __import__(nombre.replace("-", "_"))
        except ImportError:
            faltan.append(nombre)
    return {"estado": "aviso" if faltan else "ok", "detalle": ", ".join(faltan) or "completas"}


def _c_disco() -> dict:
    try:
        libre = shutil.disk_usage(config.VAULT).free / 1e9
    except OSError:
        return {"estado": "ok", "detalle": "desconocido"}
    minimo = float(config.get("guardian.espacio_minimo_gb", 5))
    if libre < minimo:
        return {"estado": "error", "detalle": f"{libre:.1f} GB libres",
                "incidencia": ("disco", "poco espacio", "alta")}
    return {"estado": "ok", "detalle": f"{libre:.1f} GB libres"}


COMPROBACIONES = {
    "lmstudio": _c_lmstudio, "sqlite": _c_sqlite, "indice": _c_indice,
    "heartbeat": _c_heartbeat, "incidencias": _c_incidencias, "locks": _c_locks,
    "logs": _c_logs, "deps": _c_deps, "disco": _c_disco,
}


def _pipeline_ocupado() -> bool:
    return heartbeat.activo()


def _cooldown_ok(clave: str) -> bool:
    return edad_segundos(config.SISTEMA / f".rep_{clave}") > int(config.get("guardian.cooldown_min", 10)) * 60


def _marcar(clave: str) -> None:
    (config.SISTEMA / f".rep_{clave}").write_text(ahora(), encoding="utf-8")


def _presupuesto_reparaciones() -> bool:
    return memoria.contador_leer("guardian.reparaciones", ventana_horas=1) < int(
        config.get("guardian.max_reparaciones_hora", 6))


def _backup() -> str:
    import zipfile
    destino_dir = config.SISTEMA / "backups"
    destino_dir.mkdir(parents=True, exist_ok=True)
    destino = destino_dir / f"backup-{ahora()[:10]}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for carpeta in (config.SISTEMA, config.PERFIL):
            for f in carpeta.rglob("*"):
                if f.is_file() and f.suffix in (".json", ".jsonl", ".md", ".sqlite"):
                    z.write(f, f.relative_to(config.VAULT))
        for f in config.MEM_DIR.rglob("*.md"):
            if "Revision" not in f.parts:
                z.write(f, f.relative_to(config.VAULT))
    for viejo in sorted(destino_dir.glob("*.zip"))[:-8]:
        viejo.unlink(missing_ok=True)
    return f"backup {destino.name} ({destino.stat().st_size/1e6:.1f} MB)"


def _reparar(clave: str) -> str:
    if clave not in config.get("guardian.reparaciones_permitidas", []):
        return ""
    if not _cooldown_ok(clave) or not _presupuesto_reparaciones():
        return ""

    if clave == "lock_obsoleto":
        from util import proceso_vivo
        hechos = []
        for ruta in (memoria.LOCK_PATH, LOCK):
            if not ruta.exists():
                continue
            try:
                pid = int(ruta.read_text(encoding="ascii").split()[0])
            except (OSError, ValueError, IndexError):
                pid = -1
            if pid > 0 and not proceso_vivo(pid):
                ruta.unlink(missing_ok=True)
                hechos.append(ruta.name)
        return f"locks liberados: {', '.join(hechos)}" if hechos else ""

    if clave == "log_rotado":
        log = config.VAULT / ".memoria" / "pipeline.log"
        if not log.exists():
            return ""
        if log.stat().st_size / 1e6 < float(config.get("guardian.log_max_mb", 5)):
            return ""
        destino = log.with_suffix(".1.log")
        destino.unlink(missing_ok=True)
        log.rename(destino)
        return f"log rotado a {destino.name}"

    if clave == "servidor_lmstudio" and not _pipeline_ocupado():
        import subprocess
        lms = shutil.which("lms") or shutil.which("lms.exe")
        if not lms:
            return ""
        subprocess.run([lms, "server", "start"], capture_output=True, timeout=120)
        return "lms server start"

    if clave == "pip_faltantes" and not _pipeline_ocupado():
        import subprocess
        faltan = _c_deps().get("detalle", "")
        if not faltan or faltan == "completas":
            return ""
        req = Path(__file__).resolve().parent / "requirements.txt"
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req)],
                       capture_output=True, timeout=900)
        return f"pip install -r requirements.txt ({faltan})"

    if clave == "indice_corrupto" and not _pipeline_ocupado():
        bak = memoria.DB_PATH.with_suffix(".sqlite.bak")
        if not bak.exists():
            return ""
        shutil.copy2(memoria.DB_PATH, memoria.DB_PATH.with_suffix(".sqlite.roto"))
        shutil.copy2(bak, memoria.DB_PATH)
        return "indice restaurado desde .bak"

    if clave == "heartbeat_colgado":
        from util import proceso_vivo
        hb = heartbeat.leer()
        if hb.get("estado") == "activo" and hb.get("pid") and not proceso_vivo(int(hb["pid"])):
            heartbeat.terminar("interrumpido")
            return "heartbeat marcado como parado"

    if clave == "backup":
        ultimo = max((p.stat().st_mtime for p in (config.SISTEMA / "backups").glob("*.zip")), default=0)
        if time.time() - ultimo < float(config.get("guardian.backup_dias", 7)) * 86400:
            return ""
        return _backup()

    return ""


def proponer(titulo: str, archivo: str, buscar: str, reemplazar: str, motivo: str) -> None:
    from util import append_linea
    append_linea(config.SISTEMA / "propuestas.jsonl", json.dumps(
        {"fecha": ahora(), "titulo": titulo, "archivo": archivo,
         "buscar": buscar, "reemplazar": reemplazar, "motivo": motivo, "aplicada": False},
        ensure_ascii=False))


def aplicar_propuestas() -> int:
    if not config.get("guardian.permitir_escribir_codigo", False):
        print("permitir_escribir_codigo = false: solo se proponen cambios.")
        return 0
    from util import leer_lineas_json
    ruta_json = config.SISTEMA / "propuestas.jsonl"
    propuestas = leer_lineas_json(ruta_json)
    aplicadas = 0
    for p in propuestas:
        if p.get("aplicada") or not p.get("buscar"):
            continue
        ruta = Path(__file__).resolve().parent / p["archivo"]
        if not ruta.exists():
            continue
        texto = ruta.read_text(encoding="utf-8")
        if p["buscar"] not in texto:
            continue
        shutil.copy2(ruta, ruta.with_suffix(ruta.suffix + ".bak"))
        ruta.write_text(texto.replace(p["buscar"], p["reemplazar"], 1), encoding="utf-8")
        p["aplicada"] = True
        aplicadas += 1
        eventos.emitir("guardian.codigo_modificado", {"archivo": p["archivo"], "titulo": p["titulo"]})
    if propuestas:
        with open(ruta_json, "w", encoding="utf-8") as f:
            for p in propuestas:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
    return aplicadas


def revisar() -> dict:
    informe = {"fecha": ahora(), "modo": config.get("guardian.modo", "observacion"),
               "checks": {}, "peor": "ok"}
    orden = {"ok": 0, "aviso": 1, "error": 2}
    for nombre in config.get("guardian.vigilar", list(COMPROBACIONES)):
        fn = COMPROBACIONES.get(nombre)
        if not fn:
            continue
        try:
            res = fn()
        except Exception as e:
            res = {"estado": "error", "detalle": f"{type(e).__name__}: {e}"[:200]}
        informe["checks"][nombre] = res
        if orden.get(res.get("estado", "ok"), 0) > orden[informe["peor"]]:
            informe["peor"] = res["estado"]
        inc = res.get("incidencia")
        if inc:
            incidencias.registrar_si_toca(
                inc[0], inc[1], inc[2], res.get("detalle", ""),
                cooldown_min=int(config.get("guardian.cooldown_incidencia_min", 15)))
        elif res.get("estado") == "ok":
            incidencias.cerrar(nombre)

    if config.get("guardian.modo", "observacion") == "reparar":
        for clave in config.get("guardian.reparaciones_permitidas", []):
            try:
                hecho = _reparar(clave)
            except Exception as e:
                hecho = f"fallo reparando {clave}: {type(e).__name__}"
            if hecho:
                memoria.contador_sumar("guardian.reparaciones", 1, ventana_horas=1)
                _marcar(clave)
                informe.setdefault("reparaciones", {})[clave] = hecho
                eventos.emitir("guardian.reparacion", {"clave": clave, "hecho": hecho})
                incidencias.registrar_si_toca("guardian", clave, "info", hecho)

    atomic_write_json(INFORME, informe)
    return informe


def main() -> int:
    if "--check" in sys.argv:
        print(f"modo    : {config.get('guardian.modo')}")
        print(f"vigilar : {config.get('guardian.vigilar')}")
        print(f"informe : {INFORME}")
        return 0
    if "--aplicar" in sys.argv:
        print(f"{aplicar_propuestas()} propuestas aplicadas")
        return 0
    if "--una-vez" in sys.argv:
        print(json.dumps(revisar(), ensure_ascii=False, indent=2))
        return 0
    intervalo = int(config.get("guardian.intervalo_segundos", 60))
    print(f"[guardian] modo {config.get('guardian.modo')} cada {intervalo}s. Ctrl+C para salir.")
    while not memoria.parado():
        with bloqueo(LOCK, vencimiento=120) as mio:
            if mio:
                informe = revisar()
                if informe["peor"] != "ok":
                    print(f"[guardian] {informe['peor']}: "
                          + ", ".join(f"{k}={v['detalle']}" for k, v in informe["checks"].items()
                                      if v.get("estado") != "ok"))
                eventos.emitir("guardian.revision", {"peor": informe["peor"]}, webhook=False)
        time.sleep(intervalo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
