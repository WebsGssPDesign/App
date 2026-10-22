# -*- coding: utf-8 -*-
"""Analisis del conocimiento: lagunas, patrones, areas y repeticion espaciada."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

import config
import escritor
import perfil
from util import ahora, hoy

_FM = re.compile(r"^(fecha|etapa|origen|tema|tags|estado|repasar|confianza|fuente|repasos):\s*(.+)$", re.M)
_LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
_MENCION = re.compile(r"\b([A-Z][A-Za-z0-9.#+-]{1,24})\b")


def escanear(limite_bytes: int = 4000) -> list[dict]:
    notas = []
    for ruta in config.MEM_DIR.rglob("*.md"):
        partes = set(ruta.parts)
        if "MOC" in partes or "Entidades" in partes:
            continue
        if ruta.name in ("Tablero.md", "AprendidoHoy.md", "AprendidoSemana.md",
                         "Huecos.md", "Conocimiento.md", "Progreso.md"):
            continue
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                crudo = f.read(limite_bytes)
        except (OSError, UnicodeDecodeError):
            continue
        fm = {m.group(1): m.group(2).strip().strip('"') for m in _FM.finditer(crudo)}
        if not fm.get("fecha"):
            continue
        cuerpo = crudo.split("---", 2)[-1] if crudo.startswith("---") else crudo
        fm["ruta"] = str(ruta.relative_to(config.VAULT)).replace("\\", "/")
        fm["titulo"] = ruta.stem
        fm["cuerpo"] = cuerpo[:limite_bytes]
        fm["enlaces"] = [l for l in _LINK.findall(cuerpo) if not l.startswith(("Entidades/",))]
        fm["temas"] = [t.strip().strip('"') for t in
                       str(fm.get("tema", "")).strip("[]").split(",") if t.strip()]
        fm["tags"] = re.findall(r"#([a-z]+)/([\w\-]+)", str(fm.get("tags", "")))
        fm["menciones"] = set(_MENCION.findall(cuerpo))
        notas.append(fm)
    return notas


def _dias(iso: str, dias: int) -> bool:
    try:
        return datetime.strptime(iso[:10], "%Y-%m-%d").date() >= date.today() - timedelta(days=dias)
    except ValueError:
        return False


def huecos(notas: list[dict] | None = None) -> dict:
    notas = notas if notas is not None else escanear()
    por_tema = Counter(t for n in notas for t in n["temas"])
    sin_cubrir = [i for i in perfil.intereses() if por_tema.get(i, 0) == 0]
    flojos = [t for t, c in por_tema.items() if c == 1]
    huerfanas = [n["ruta"] for n in notas if not n["enlaces"]]
    aisladas = [n["ruta"] for n in notas
                if not any(o["enlaces"] and n["ruta"] in " ".join(o["enlaces"]) for o in notas)
                and n["ruta"] not in huerfanas]
    sin_material = []
    try:
        from util import leer_json
        estado_sk = leer_json(config.ESTADO_DIR / "skills.json", {}) or {}
        sin_material = [k for k, v in (estado_sk.get("saltadas") or {}).items()
                        if "material" in str(v).lower()][:20]
    except Exception:
        pass
    return {"sin_cubrir": sin_cubrir, "flojos": flojos, "huerfanas": huerfanas,
            "aisladas": aisladas, "sin_material": sin_material,
            "total": len(sin_cubrir) + len(flojos) + len(sin_material)}


def patrones(notas: list[dict] | None = None) -> dict:
    notas = notas if notas is not None else escanear()
    por_dia = Counter(n["fecha"][:10] for n in notas)
    racha = 0
    for i in range(60):
        if (date.today() - timedelta(days=i)).isoformat() in por_dia:
            racha += 1
        elif i:
            break
    return {"por_dia": por_dia,
            "por_etapa": Counter(n.get("etapa", "?") for n in notas),
            "por_origen": Counter(n.get("origen", "local") for n in notas),
            "racha_dias": racha,
            "ultimos_7": sum(v for k, v in por_dia.items() if _dias(k, 7)),
            "ultimos_30": sum(v for k, v in por_dia.items() if _dias(k, 30))}


def areas(notas: list[dict] | None = None) -> dict:
    notas = notas if notas is not None else escanear()
    por_tema: dict[str, list[dict]] = defaultdict(list)
    for n in notas:
        for t in n["temas"]:
            por_tema[t].append(n)
    dominadas, activas, emergentes = [], [], []
    for tema, grupo in por_tema.items():
        altas = sum(1 for n in grupo if n.get("confianza") == "alta")
        recientes = sum(1 for n in grupo if _dias(n["fecha"], 30))
        nuevas = sum(1 for n in grupo if _dias(n["fecha"], 14))
        primera = min(n["fecha"] for n in grupo)
        if len(grupo) >= 4 and altas >= 2 and recientes >= 2:
            dominadas.append((tema, len(grupo), altas))
        elif recientes:
            activas.append((tema, len(grupo), recientes))
        if nuevas and _dias(primera, 21) and len(grupo) <= 3:
            emergentes.append((tema, len(grupo)))
    orden = lambda x: -x[1]
    return {"dominadas": sorted(dominadas, key=orden),
            "activas": sorted(activas, key=orden),
            "emergentes": sorted(emergentes, key=orden)}


def siguiente_repaso(repasos: int) -> str:
    dias = config.get("tablero.repaso_dias", [1, 3, 7, 21, 60])
    salto = dias[min(repasos, len(dias) - 1)]
    return (date.today() + timedelta(days=int(salto))).isoformat()


def procesar_revisiones(notas: list[dict] | None = None) -> int:
    """Notas con estado 'revisada': sube un escalon el repaso y vuelve a 'sin-revisar'."""
    notas = notas if notas is not None else escanear()
    avanzadas = 0
    for n in notas:
        if str(n.get("estado", "")).lower() != "revisada":
            continue
        repasos = int(n.get("repasos", 0) or 0) + 1
        ruta = config.VAULT / n["ruta"]
        try:
            cuerpo = ruta.read_text(encoding="utf-8")
        except OSError:
            continue
        cuerpo = re.sub(r"^estado:.*$", "estado: sin-revisar", cuerpo, count=1, flags=re.M)
        cuerpo = re.sub(r"^repasar:.*$", f"repasar: {siguiente_repaso(repasos)}", cuerpo, count=1, flags=re.M)
        if re.search(r"^repasos:", cuerpo, flags=re.M):
            cuerpo = re.sub(r"^repasos:.*$", f"repasos: {repasos}", cuerpo, count=1, flags=re.M)
        else:
            cuerpo = cuerpo.replace("estado: sin-revisar", f"estado: sin-revisar\nrepasos: {repasos}", 1)
        ruta.write_text(cuerpo, encoding="utf-8")
        avanzadas += 1
    return avanzadas


def cola_repaso(notas: list[dict] | None = None) -> list[dict]:
    notas = notas if notas is not None else escanear()
    vencidas = [n for n in notas if str(n.get("repasar", ""))[:10] <= hoy()
                and str(n.get("estado", "")).lower() != "revisada"]
    return sorted(vencidas, key=lambda n: str(n.get("repasar", "")))


def render_huecos(notas: list[dict] | None = None) -> str:
    h = huecos(notas)
    l = ["# Huecos de conocimiento", "",
         f"Actualizado: {ahora()} — {h['total']} senales", "",
         "> Detectado automaticamente. Un hueco no es un error: es una pista de por donde seguir.", ""]
    if h["sin_cubrir"]:
        l += ["## Intereses sin ninguna nota", ""] + [f"- [[{t}]]" for t in h["sin_cubrir"]] + [""]
    if h["sin_material"]:
        l += ["## Temas donde no hubo material suficiente", ""] + [f"- {t}" for t in h["sin_material"]] + [""]
    if h["flojos"]:
        l += ["## Conceptos con una sola mencion", ""] + [f"- [[{t}]]" for t in h["flojos"][:25]] + [""]
    if h["huerfanas"]:
        l += ["## Notas sin ningun enlace saliente", ""] + [f"- {escritor.wikilink(r)}" for r in h["huerfanas"][:25]] + [""]
    if h["aisladas"]:
        l += ["## Notas que nadie enlaza", ""] + [f"- {escritor.wikilink(r)}" for r in h["aisladas"][:25]] + [""]
    return "\n".join(l) + "\n"


def render_conocimiento(notas: list[dict] | None = None) -> str:
    a = areas(notas)
    l = ["# Mapa de conocimiento", "", f"Actualizado: {ahora()}", ""]
    for titulo, grupo, nota in (
            ("Areas dominadas", a["dominadas"], "4 o mas notas, con fuentes de confianza alta"),
            ("Areas activas", a["activas"], "con actividad en los ultimos 30 dias"),
            ("Areas emergentes", a["emergentes"], "aparecidas en las ultimas 3 semanas")):
        l += [f"## {titulo}", "", f"_{nota}_", ""]
        l += [f"- [[{t}]] — {n} notas" for t, n, *_ in grupo[:30]] or ["- _ninguna_"]
        l.append("")
    return "\n".join(l) + "\n"


def actualizar() -> dict:
    notas = escanear()
    fm = {"fecha": hoy(), "etapa": "analisis", "origen": "sistema",
          "estado": "generado", "generado": True, "propietario": "analisis"}
    escritor.escribir("LLM-Memoria/Huecos.md", render_huecos(notas), fm, "analisis", sobrescribir=True)
    escritor.escribir("LLM-Memoria/Conocimiento.md", render_conocimiento(notas), fm, "analisis", sobrescribir=True)
    return {"huecos": huecos(notas)["total"], "notas": len(notas)}


def main() -> int:
    import sys
    if "--check" in sys.argv:
        n = escanear()
        print(f"notas       : {len(n)}")
        print(f"huecos      : {huecos(n)['total']}")
        print(f"cola repaso : {len(cola_repaso(n))}")
        return 0
    if "--revisar" in sys.argv:
        print(f"{procesar_revisiones()} notas reprogramadas")
        return 0
    print(actualizar())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
