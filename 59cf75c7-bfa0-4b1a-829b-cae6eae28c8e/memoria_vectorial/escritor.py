# -*- coding: utf-8 -*-
"""Unico punto de escritura en la boveda. Frontmatter seguro, papelera, auditoria."""
from __future__ import annotations

import contextlib
import json
import re
import shutil
from pathlib import Path

import config
from util import ahora, append_linea, atomic_write_text

AUDITORIA = config.SISTEMA / "auditoria.jsonl"
_PERMITIDAS = tuple(config.RUTAS_ESCRIBIBLES)
_PELIGROSO = re.compile(r'[\x00-\x1f<>:"|?*]')


def rel_valida(rel: str) -> Path:
    """Normaliza una ruta relativa a la boveda y evita salir de ella."""
    limpio = str(rel).replace("\\", "/").strip("/")
    destino = (config.VAULT / limpio).resolve()
    if not str(destino).lower().startswith(str(config.VAULT.resolve()).lower()):
        raise ValueError(f"ruta fuera de la boveda: {rel}")
    return destino


def en_raiz_permitida(destino: Path) -> bool:
    return any(str(destino).lower().startswith(str(r.resolve()).lower()) for r in _PERMITIDAS)


def sanear_nombre(nombre: str, maximo: int = 80) -> str:
    limpio = _PELIGROSO.sub("-", str(nombre)).strip(" .-")
    limpio = re.sub(r"\s+", " ", limpio)
    return (limpio or "sin-nombre")[:maximo]


def _yaml_valor(valor) -> str:
    if valor is None:
        return '""'
    if isinstance(valor, bool):
        return "true" if valor else "false"
    if isinstance(valor, (int, float)):
        return str(valor)
    if isinstance(valor, (list, tuple)):
        return "[" + ", ".join(_yaml_valor(v) for v in valor) + "]"
    texto = str(valor).replace("\\", "\\\\").replace('"', '\\"')
    texto = re.sub(r"\s+", " ", texto).strip()
    return f'"{texto}"'


def frontmatter(datos: dict) -> str:
    lineas = ["---"]
    for clave, valor in datos.items():
        lineas.append(f"{clave}: {_yaml_valor(valor)}")
    lineas.append("---")
    return "\n".join(lineas) + "\n"


def wikilink(rel: str, texto: str | None = None) -> str:
    limpio = str(rel).replace("\\", "/")
    if limpio.lower().endswith(".md"):
        limpio = limpio[:-3]
    etiqueta = texto or limpio.rsplit("/", 1)[-1]
    return f"[[{limpio}|{etiqueta}]]"


def enlace_obsidian(rel: str) -> str:
    limpio = str(rel).replace("\\", "/")
    if limpio.lower().endswith(".md"):
        limpio = limpio[:-3]
    return f"obsidian://open?vault={config.VAULT.name}&file={limpio}"


def _auditar(accion: str, rel: str, propietario: str, detalle: str = "") -> None:
    try:
        append_linea(AUDITORIA, json.dumps(
            {"fecha": ahora(), "accion": accion, "ruta": str(rel),
             "propietario": propietario, "detalle": detalle}, ensure_ascii=False))
    except OSError:
        pass


def _a_papelera(destino: Path) -> Path:
    rel = destino.relative_to(config.VAULT)
    marca = ahora().replace(":", "").replace(" ", "-")
    copia = config.PAPELERA / marca / rel
    copia.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(destino), str(copia))
    return copia


def escribir(rel: str, cuerpo: str, fm: dict | None = None, propietario: str = "sistema",
             sobrescribir: bool = False, backup: bool = True) -> Path:
    """Escribe una nota. Si existe, guarda .bak."""
    destino = rel_valida(rel)
    if not en_raiz_permitida(destino):
        raise ValueError(f"fuera de las raices permitidas: {rel}")
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists() and backup:
        with contextlib.suppress(OSError):
            shutil.copy2(destino, destino.with_name(destino.name + ".bak"))
    texto = (frontmatter(fm) if fm else "") + cuerpo
    if not texto.endswith("\n"):
        texto += "\n"
    atomic_write_text(destino, texto)
    _auditar("escribir", rel, propietario, f"{len(texto)}b")
    return destino


def mover(rel_origen: str, rel_destino: str, propietario: str = "sistema") -> Path:
    origen = rel_valida(rel_origen)
    destino = rel_valida(rel_destino)
    if not origen.exists():
        raise FileNotFoundError(rel_origen)
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(origen), str(destino))
    _auditar("mover", rel_origen, propietario, f"-> {rel_destino}")
    return destino


def eliminar(rel: str, propietario: str = "sistema") -> Path | None:
    """Nunca borra de verdad: mueve a Sistema/papelera/<marca>/."""
    destino = rel_valida(rel)
    if not destino.exists():
        return None
    copia = _a_papelera(destino)
    _auditar("eliminar", rel, propietario, f"-> {copia}")
    return copia


def indexar(rel: str) -> bool:
    """Indexa al instante si el indice esta disponible. Nunca lanza."""
    try:
        import memoria
        return memoria.indexar_archivo(str(rel).replace("\\", "/")) > 0
    except Exception:
        return False
