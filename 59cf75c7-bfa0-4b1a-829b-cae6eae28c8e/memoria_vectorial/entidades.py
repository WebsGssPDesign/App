# -*- coding: utf-8 -*-
"""Entidades del grafo. Paginas de entidad con backlinks en wikilink."""
from __future__ import annotations

import re
from collections import Counter, defaultdict

import analisis
import config
import escritor
import perfil
from util import hoy

CARPETA = "LLM-Memoria/Entidades"
_IGNORAR = {"El", "La", "Los", "Las", "Un", "Una", "Este", "Esta", "Todo", "Todos",
            "Cuando", "Como", "Donde", "Porque", "Pero", "Tambien", "Ademas", "Sin"}


def conocidas() -> set[str]:
    base = set(perfil.tecnologias()) | set(perfil.intereses()) | set(perfil.objetivos())
    try:
        from util import leer_json
        base |= set((leer_json(config.SISTEMA / "entidades.json", {}) or {}).get("extra", []))
    except Exception:
        pass
    return {b for b in base if 2 < len(b) < 40}


def candidatas(notas: list[dict]) -> Counter:
    conocidas_min = {c.lower(): c for c in conocidas()}
    contador: Counter = Counter()
    for n in notas:
        for t in n["temas"]:
            contador[conocidas_min.get(t.lower(), t)] += 3
        for c in n["menciones"]:
            if c in _IGNORAR or len(c) < 3:
                continue
            contador[conocidas_min.get(c.lower(), c)] += 1
    return Counter({k: v for k, v in contador.items() if v >= 3})


def _rel(nombre: str) -> str:
    return f"{CARPETA}/{escritor.sanear_nombre(nombre, 60)}.md"


def construir(notas: list[dict] | None = None, maximo: int = 120) -> int:
    notas = notas if notas is not None else analisis.escanear()
    contador = candidatas(notas)
    if not contador:
        return 0
    top = [n for n, _ in contador.most_common(maximo)]

    menciones: dict[str, list[dict]] = defaultdict(list)
    for n in notas:
        texto = " ".join(n["temas"]) + " " + n["cuerpo"]
        for entidad in top:
            if re.search(rf"\b{re.escape(entidad)}\b", texto, flags=re.I):
                menciones[entidad].append(n)

    creadas = 0
    for entidad in top:
        grupo = menciones.get(entidad) or []
        if len(grupo) < 2:
            continue
        fechas = sorted(n["fecha"] for n in grupo)
        co = Counter()
        for n in grupo:
            for t in n["temas"]:
                if t.lower() != entidad.lower():
                    co[t] += 1
        confianza = "alta" if any(n.get("confianza") == "alta" for n in grupo) else "media"
        cuerpo = [f"# {entidad}", "",
                  "> Entidad detectada por el sistema. Se regenera sola.", "",
                  f"- Menciones: {len(grupo)}",
                  f"- Primera vez: {fechas[0][:10]}",
                  f"- Ultima vez: {fechas[-1][:10]}",
                  f"- Confianza: {confianza}", ""]
        if co:
            cuerpo += ["## Relacionadas", ""] + [f"- [[{t}]] ({c})" for t, c in co.most_common(10)] + [""]
        cuerpo += ["## Notas que la mencionan", ""]
        cuerpo += [f"- {n['fecha'][:10]} · {escritor.wikilink(n['ruta'])}"
                   for n in sorted(grupo, key=lambda x: x["fecha"], reverse=True)[:60]]
        escritor.escribir(_rel(entidad), "\n".join(cuerpo) + "\n",
                          {"fecha": hoy(), "tipo": "entidad", "origen": "sistema",
                           "etapa": "grafo", "tema": f"[{entidad}]", "tags": "[tipo/entidad]",
                           "estado": "generado", "confianza": confianza, "generado": True},
                          "entidades", sobrescribir=True)
        creadas += 1
    return creadas


def enlazar_notas(notas: list[dict] | None = None, maximo_por_nota: int = 6) -> int:
    """Anade [[Entidad]] en la primera mencion dentro de notas generadas."""
    notas = notas if notas is not None else analisis.escanear()
    entidades = sorted({c for c in candidatas(notas)}, key=len, reverse=True)[:120]
    tocadas = 0
    for n in notas:
        ruta = config.VAULT / n["ruta"]
        try:
            texto = ruta.read_text(encoding="utf-8")
        except OSError:
            continue
        original = texto
        puestos = 0
        for entidad in entidades:
            if puestos >= maximo_por_nota:
                break
            if f"[[{entidad}]]" in texto or f"|{entidad}]]" in texto:
                continue
            nuevo, cuenta = re.subn(rf"(?<![\w\[])({re.escape(entidad)})(?![\w\]])",
                                   rf"[[{entidad}]]", texto, count=1)
            if cuenta:
                texto = nuevo
                puestos += 1
        if texto != original:
            ruta.write_text(texto, encoding="utf-8")
            tocadas += 1
    return tocadas


def main() -> int:
    import sys
    notas = analisis.escanear()
    if "--check" in sys.argv:
        print(f"candidatas : {len(candidatas(notas))}")
        print(f"carpeta    : {CARPETA}")
        return 0
    print(f"{construir(notas)} paginas de entidad")
    if "--enlazar" in sys.argv:
        print(f"{enlazar_notas(notas)} notas enlazadas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
