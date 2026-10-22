# -*- coding: utf-8 -*-
"""Perfil persistente del usuario. Alimenta prompts, relevancia web y busquedas."""
from __future__ import annotations

import config
from util import leer_json

SEMILLA = {
    "perfil_usuario.json": {
        "version": 1,
        "nombre": "Guillermo Samuel Simones Primera",
        "idioma": "es",
        "filosofia": ["simplicidad", "control manual", "minimo numero de dependencias",
                      "primero funciona, luego optimiza"],
        "herramientas": ["LM Studio", "Obsidian", "VS Code", "OrderCode", "n8n", "Git", "Hostinger"],
        "stack_por_defecto": {
            "frontend": ["HTML5", "CSS Vanilla", "JavaScript Vanilla"],
            "framework": ["React", "Next.js"],
            "datos": ["MongoDB"],
        },
        "reglas_inferencia": [
            "Si pide una app o web sin especificar stack, usar stack_por_defecto.",
            "Preferir HTML5 + CSS + JS vanilla antes que un framework salvo que lo pida.",
            "No proponer dependencias nuevas si la stdlib resuelve el problema.",
        ],
    },
    "intereses.json": {
        "version": 1,
        "principales": ["HTML5", "CSS Vanilla", "JavaScript Vanilla", "React", "Next.js",
                        "MongoDB", "Obsidian", "LM Studio", "IA local", "n8n", "automatizacion",
                        "negocios digitales", "desarrollo web", "sistemas de memoria"],
        "peso": {"IA local": 1.0, "sistemas de memoria": 1.0, "automatizacion": 0.9,
                 "desarrollo web": 0.8, "n8n": 0.8, "Obsidian": 0.8,
                 "React": 0.7, "Next.js": 0.7, "MongoDB": 0.6},
        "secundarios": [],
    },
    "objetivos.json": {
        "version": 1,
        "activos": ["desarrollar aplicaciones reales", "construir negocios digitales",
                    "automatizar tareas", "construir un segundo cerebro local"],
        "peso": {"construir un segundo cerebro local": 1.0, "automatizar tareas": 0.9},
    },
}

_cache: dict | None = None


def _ruta(nombre: str):
    return config.PERFIL / nombre


def asegurar() -> bool:
    """Crea los JSON del perfil si faltan. Nunca sobrescribe los existentes."""
    creado = False
    config.PERFIL.mkdir(parents=True, exist_ok=True)
    for nombre, contenido in SEMILLA.items():
        ruta = _ruta(nombre)
        if not ruta.exists():
            from util import ahora, atomic_write_json
            contenido = dict(contenido)
            contenido["actualizado"] = ahora()
            atomic_write_json(ruta, contenido)
            creado = True
    return creado


def cargar(recargar: bool = False) -> dict:
    global _cache
    if _cache is not None and not recargar:
        return _cache
    asegurar()
    datos = {}
    for nombre, defecto in SEMILLA.items():
        leido = leer_json(_ruta(nombre), {})
        base = dict(defecto)
        base.update(leido or {})
        datos[nombre.replace(".json", "")] = base
    _cache = datos
    return datos


def nombre() -> str:
    return str(cargar()["perfil_usuario"].get("nombre", ""))


def intereses() -> list[str]:
    d = cargar()["intereses"]
    return list(d.get("principales", [])) + list(d.get("secundarios", []))


def pesos() -> dict:
    return dict(cargar()["intereses"].get("peso", {}))


def objetivos() -> list[str]:
    return list(cargar()["objetivos"].get("activos", []))


def tecnologias() -> list[str]:
    p = cargar()["perfil_usuario"]
    salida = list(p.get("herramientas", []))
    for grupo in (p.get("stack_por_defecto") or {}).values():
        salida += list(grupo)
    return sorted(set(salida))


def como_contexto(maximo: int = 1200) -> str:
    p = cargar()
    lineas = [
        f"Usuario: {p['perfil_usuario'].get('nombre', '')}",
        f"Intereses: {', '.join(intereses())}",
        f"Objetivos: {', '.join(objetivos())}",
        f"Herramientas: {', '.join(p['perfil_usuario'].get('herramientas', []))}",
        f"Filosofia: {', '.join(p['perfil_usuario'].get('filosofia', []))}",
        "Reglas de inferencia:",
    ]
    lineas += [f"  - {r}" for r in p["perfil_usuario"].get("reglas_inferencia", [])]
    return "\n".join(lineas)[:maximo]


def puntuar_relevancia(texto: str) -> float:
    """0.0 a 1.0. Sin embeddings disponibles, cae a coincidencia de palabras."""
    texto_min = (texto or "").lower()
    if not texto_min.strip():
        return 0.0
    pesos = pesos()
    terminos = intereses() + objetivos()
    if not terminos:
        return 0.5
    total = encontrados = 0.0
    for termino in terminos:
        t = termino.lower()
        if not t:
            continue
        peso = float(pesos.get(termino, 0.5))
        total += peso
        if t in texto_min:
            encontrados += peso
    base = (encontrados / total) if total else 0.0
    try:
        import memoria
        vec = memoria.embed([texto[:1500]], tipo="query")
        ref = memoria.embed([como_contexto()], tipo="query")
        if vec is not None and ref is not None:
            sim = float((vec @ ref.T)[0][0])
            return max(0.0, min(1.0, 0.65 * sim + 0.35 * base))
    except Exception:
        pass
    return min(1.0, base)


def es_relevante(texto: str) -> bool:
    return puntuar_relevancia(texto) >= float(config.get("web.min_relevancia", 0.45))


def espejo() -> str:
    """Escribe Perfil/perfil_usuario.md. Indexable y legible en Obsidian."""
    import escritor
    from util import hoy
    p = cargar()["perfil_usuario"]
    lineas = [f"# Perfil de {p.get('nombre', '')}", "",
              "> Espejo legible de `Perfil\\perfil_usuario.json`. Se regenera solo.", ""]
    for titulo, clave in (("Intereses", None), ("Objetivos", None), ("Herramientas", "herramientas"),
                          ("Filosofia", "filosofia"), ("Stack por defecto", "stack_por_defecto"),
                          ("Reglas de inferencia", "reglas_inferencia")):
        lineas += [f"## {titulo}", ""]
        if clave is None:
            datos = intereses() if titulo == "Intereses" else objetivos()
            lineas += [f"- {d}" for d in datos]
        else:
            valor = p.get(clave)
            if isinstance(valor, dict):
                for k, v in valor.items():
                    lineas.append(f"- **{k}**: {', '.join(v) if isinstance(v, list) else v}")
            else:
                lineas += [f"- {v}" for v in (valor or [])]
        lineas.append("")
    lineas += ["## Pesos", ""] + [f"- {k}: {v}" for k, v in pesos().items()]
    rel = "Perfil/perfil_usuario.md"
    escritor.escribir(rel, "\n".join(lineas) + "\n",
                      {"fecha": hoy(), "origen": "perfil", "tipo": "perfil",
                       "etapa": "perfil", "confianza": "alta", "generado": True,
                       "propietario": "perfil"}, "perfil", sobrescribir=True)
    return rel


def main() -> int:
    import sys
    if "--check" in sys.argv:
        asegurar()
        for nombre_archivo in SEMILLA:
            ruta = _ruta(nombre_archivo)
            print(f"  {nombre_archivo:<24} {'ok' if ruta.exists() else 'FALTA'}  {ruta}")
        print(f"  intereses: {len(intereses())} | objetivos: {len(objetivos())}")
        return 0
    if "--espejo" in sys.argv:
        print(f"escrito: {espejo()}")
        return 0
    print(como_contexto())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
