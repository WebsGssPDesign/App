# -*- coding: utf-8 -*-
"""Latido del pipeline. Un escritor, muchos lectores. Nunca lanza."""
from __future__ import annotations

import os
from pathlib import Path

import config
from util import ahora, atomic_write_json, leer_json

RUTA = config.SISTEMA / "heartbeat.json"

_VACIO = {"estado": "parado", "paso": "", "detalle": "", "pid": 0,
          "inicio": "", "actualizado": "", "pasos": [], "resultado": ""}


def _escribir(datos: dict) -> None:
    try:
        atomic_write_json(RUTA, datos)
    except OSError:
        pass


def leer() -> dict:
    datos = dict(_VACIO)
    datos.update(leer_json(RUTA, {}) or {})
    return datos


def latir(paso: str, detalle: str = "", estado: str = "activo") -> None:
    datos = leer()
    if datos.get("estado") != "activo" or datos.get("paso") != paso:
        datos["inicio"] = ahora()
    datos.update({"estado": estado, "paso": paso, "detalle": detalle,
                  "pid": os.getpid(), "actualizado": ahora()})
    pasos = datos.get("pasos") or []
    if paso and (not pasos or pasos[-1].get("paso") != paso):
        pasos.append({"paso": paso, "inicio": ahora(), "fin": ""})
    datos["pasos"] = pasos[-40:]
    _escribir(datos)


def terminar(resultado: str = "ok") -> None:
    datos = leer()
    pasos = datos.get("pasos") or []
    if pasos and not pasos[-1].get("fin"):
        pasos[-1]["fin"] = ahora()
    datos.update({"estado": "parado", "resultado": resultado,
                  "pasos": pasos, "actualizado": ahora()})
    _escribir(datos)


def segundos_sin_latir() -> float:
    from util import edad_segundos
    return edad_segundos(RUTA)


def activo(umbral: int = 0) -> bool:
    if umbral <= 0:
        umbral = int(config.get("guardian.heartbeat_vencido_seg", 300))
    datos = leer()
    return datos.get("estado") == "activo" and segundos_sin_latir() < umbral
