# -*- coding: utf-8 -*-
"""Genera la capa Obsidian de visibilidad. Idempotente: regenera y sustituye."""
from __future__ import annotations

import re
from collections import Counter
from datetime import date, timedelta

import config
import escritor
import heartbeat
import incidencias
import metricas
from util import ahora, hoy

PROPIETARIO = "tablero"
_CABECERA = "<!-- generado por tablero.py. No editar a mano. -->\n"
_FM_RE = re.compile(r"^(fecha|etapa|origen|tema|tags|estado|repasar|confianza):\s*(.+)$", re.M)


def _escanear_notas() -> list[dict]:
    notas: list[dict] = []
    for ruta in config.MEM_DIR.rglob("*.md"):
        partes = set(ruta.parts)
        if "Revision" in partes or "MOC" in partes or "Entidades" in partes:
            continue
        if ruta.name in ("Tablero.md", "AprendidoHoy.md", "AprendidoSemana.md",
                         "Huecos.md", "Conocimiento.md", "Progreso.md"):
            continue
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                cabeza = f.read(1200)
        except (OSError, UnicodeDecodeError):
            continue
        datos = {m.group(1): m.group(2).strip().strip('"') for m in _FM_RE.finditer(cabeza)}
        if not datos.get("fecha"):
            continue
        datos["ruta"] = str(ruta.relative_to(config.VAULT)).replace("\\", "/")
        datos["titulo"] = ruta.stem
        notas.append(datos)
    return notas


def _contar_skills() -> list[str]:
    if not config.SKILLS_DIR.exists():
        return []
    return sorted(p.name for p in config.SKILLS_DIR.iterdir() if p.is_dir())


def _grafico(por_dia: dict[str, int], dias: int) -> str:
    fin = date.today()
    serie = [(fin - timedelta(days=d)).isoformat() for d in range(dias - 1, -1, -1)]
    valores = [por_dia.get(f, 0) for f in serie]
    etiquetas = [f[5:] for f in serie[:: max(1, dias // 6)]]
    alto = max(valores + [1])
    return ("```mermaid\nxychart-beta\n"
            f'    title "Notas generadas por dia (ultimos {dias})"\n'
            f"    x-axis [{', '.join(etiquetas)}]\n"
            f'    y-axis "notas" 0 --> {alto}\n'
            f"    bar [{', '.join(str(v) for v in valores)}]\n```")


def _tablero(notas: list[dict]) -> str:
    hb = heartbeat.leer()
    inc = incidencias.resumen()
    rend = metricas.rendimiento()
    por_dia = Counter(n.get("fecha", "")[:10] for n in notas)
    por_etapa = Counter(n.get("etapa", "?") for n in notas)
    por_origen = Counter(n.get("origen", "local") for n in notas)
    temas = Counter(t.strip() for n in notas for t in str(n.get("tema", "")).strip("[]").split(",") if t.strip())
    skills = _contar_skills()
    semilla = (date.today() - timedelta(days=6)).isoformat()
    semana = [n for n in notas if n.get("fecha", "")[:10] >= semilla]
    recientes = sorted(notas, key=lambda n: n.get("fecha", ""), reverse=True)[: int(config.get("tablero.max_listado", 25))]

    l = [_CABECERA, "# Tablero", "", f"Actualizado: {ahora()}", ""]
    l += ["## Estado", "",
          f"- Pipeline: **{'ACTIVO' if heartbeat.activo() else 'parado'}**"
          + (f" (paso: {hb.get('paso')}, {hb.get('actualizado')})" if hb.get("paso") else ""),
          f"- Ultimo resultado: {hb.get('resultado') or 'sin datos'}",
          f"- Incidencias abiertas: **{inc['total']}**",
          f"- Notas totales: **{len(notas)}** | esta semana: {len(semana)} | hoy: {por_dia.get(hoy(), 0)}",
          f"- Skills: {len(skills)}", ""]
    if inc["total"]:
        l += ["### Incidencias abiertas", ""]
        for i in inc["peores"][:8]:
            l.append(f"- `{i.get('gravedad')}` **{i.get('componente')}** — {str(i.get('error'))[:110]} ({i.get('estado')}, {i.get('reintentos')}x)")
        l.append("")
    l += ["## Actividad", "", _grafico(por_dia, int(config.get("tablero.dias_grafico", 30))), ""]
    l += ["### Por etapa", ""] + [f"- {k}: {v}" for k, v in por_etapa.most_common()] + [""]
    l += ["### Por origen", ""] + [f"- {k}: {v}" for k, v in por_origen.most_common()] + [""]
    l += ["## Temas principales", ""] + [f"- [[{t}]] ({c})" for t, c in temas.most_common(20)] + [""]
    l += ["## Rendimiento (hoy)", "",
          f"- Archivos procesados: {rend['procesados']} (ok {rend['ok']}, fallos {rend['fallos']})",
          f"- Tiempo total: {rend['segundos_totales']}s", ""]
    l += ["## Notas recientes", ""] + [f"- {n['fecha']} · {escritor.wikilink(n['ruta'])}" for n in recientes] + [""]
    l += ["## Skills", ""] + [f"- {s}" for s in skills] + [""]
    l += ["## Enlaces", "", "- [[Huecos]] · [[Conocimiento]] · [[Revision/Cola]]",
          "- [[AprendidoHoy]] · [[AprendidoSemana]]", ""]
    return "\n".join(l)


def _listado(titulo: str, notas: list[dict], desde: str) -> str:
    filtradas = sorted((n for n in notas if n.get("fecha", "")[:10] >= desde),
                       key=lambda n: n.get("fecha", ""), reverse=True)
    l = [_CABECERA, f"# {titulo}", "", f"Actualizado: {ahora()} — {len(filtradas)} entradas", ""]
    if not filtradas:
        l += ["_Nada todavia._", ""]
    for n in filtradas:
        l.append(f"- {n['fecha']} · {escritor.wikilink(n['ruta'])} · `{n.get('etapa','?')}`")
    return "\n".join(l) + "\n"


def _cola(notas: list[dict]) -> str:
    pendientes = [n for n in notas if str(n.get("repasar", ""))[:10] <= hoy()]
    pendientes.sort(key=lambda n: str(n.get("repasar", "")))
    l = [_CABECERA, "# Cola de revision", "", f"Actualizado: {ahora()} — {len(pendientes)} pendientes", ""]
    if not pendientes:
        l += ["_Nada pendiente._", ""]
    for n in pendientes[:60]:
        l.append(f"- [ ] {n.get('repasar','?')} · {escritor.wikilink(n['ruta'])}")
    return "\n".join(l) + "\n"


def _mocs(notas: list[dict]) -> int:
    minimo = int(config.get("tablero.min_notas_moc", 3))
    por_carpeta: dict[str, list[dict]] = {}
    for n in notas:
        partes = n["ruta"].split("/")
        if len(partes) < 3 or partes[0] != config.MEM_DIR.name:
            continue
        por_carpeta.setdefault(partes[1], []).append(n)
    creados = 0
    fm = {"fecha": hoy(), "etapa": "moc", "origen": "sistema",
          "estado": "generado", "generado": True}
    for carpeta, grupo in por_carpeta.items():
        if len(grupo) < minimo:
            continue
        l = [f"# MOC {carpeta}", "", f"{len(grupo)} notas.", ""]
        for n in sorted(grupo, key=lambda x: x["fecha"], reverse=True):
            l.append(f"- {n['fecha'][:10]} · {escritor.wikilink(n['ruta'])}")
        escritor.escribir(f"LLM-Memoria/MOC/MOC {carpeta}.md", "\n".join(l) + "\n",
                          fm, PROPIETARIO, sobrescribir=True)
        creados += 1
    return creados


def _diario(notas: list[dict]) -> bool:
    dia = hoy()
    de_hoy = sorted((n for n in notas if n.get("fecha", "")[:10] == dia),
                    key=lambda n: n.get("fecha", ""))
    rel = f"{config.DIARIO.name}/{dia}.md"
    ruta = config.VAULT / rel
    cuerpo_previo = ""
    if ruta.exists():
        try:
            cuerpo_previo = ruta.read_text(encoding="utf-8").split("## Aprendizaje", 1)[0].rstrip()
        except OSError:
            cuerpo_previo = ""
    if not cuerpo_previo:
        cuerpo_previo = f"# {dia}\n\n## Notas del dia\n\n_Libre._"
    bloque = ["", "## Aprendizaje", "",
              f"_{len(de_hoy)} entradas registradas por el sistema._", ""]
    if de_hoy:
        bloque += [f"- {n['fecha'][11:16]} · {escritor.wikilink(n['ruta'])} · `{n.get('etapa','?')}`"
                   for n in de_hoy]
    else:
        bloque.append("_Nada todavia._")
    bloque += ["", "## Repaso", "", "- [ ] pendiente", ""]
    escritor.escribir(rel, cuerpo_previo + "\n" + "\n".join(bloque) + "\n",
                      {"fecha": dia, "tipo": "diario", "origen": "sistema", "generado": True},
                      PROPIETARIO, sobrescribir=True)
    return True


def actualizar() -> dict:
    notas = _escanear_notas()
    fm_base = {"fecha": hoy(), "etapa": "tablero", "origen": "sistema",
               "estado": "generado", "generado": True, "propietario": PROPIETARIO}
    escritor.escribir("LLM-Memoria/Tablero.md", _tablero(notas), fm_base, PROPIETARIO, sobrescribir=True)
    escritor.escribir("LLM-Memoria/AprendidoHoy.md", _listado("Aprendido hoy", notas, hoy()), fm_base, PROPIETARIO, sobrescribir=True)
    escritor.escribir("LLM-Memoria/AprendidoSemana.md",
                      _listado("Aprendido esta semana", notas,
                               (date.today() - timedelta(days=6)).isoformat()), fm_base, PROPIETARIO, sobrescribir=True)
    escritor.escribir("LLM-Memoria/Revision/Cola.md", _cola(notas), fm_base, PROPIETARIO, sobrescribir=True)
    _mocs(notas)
    _diario(notas)
    print(escritor.enlace_obsidian("LLM-Memoria/Tablero.md"))
    return {"notas": len(notas)}


def actualizar_si_toca(segundos: int = 90) -> bool:
    from util import edad_segundos
    if edad_segundos(config.MEM_DIR / "Tablero.md") < segundos:
        return False
    actualizar()
    return True


def main() -> int:
    import sys
    if "--check" in sys.argv:
        print(f"notas detectadas: {len(_escanear_notas())}")
        return 0
    print(actualizar())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
