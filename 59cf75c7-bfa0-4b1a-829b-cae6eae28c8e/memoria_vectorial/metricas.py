# -*- coding: utf-8 -*-
"""Metricas por archivo procesado. Append-only, un solo os.write por linea."""
from __future__ import annotations

import json

import config
from util import ahora, append_linea, leer_lineas_json

RUTA = config.SISTEMA / "metricas.jsonl"


def registrar(etapa: str, archivo: str = "", segundos: float = 0.0,
              entrada: int = 0, salida: int = 0, resultado: str = "ok",
              modelo: str = "", extra: dict | None = None) -> None:
    fila = {
        "fecha": ahora(), "etapa": etapa, "archivo": archivo[:300],
        "segundos": round(float(segundos), 3), "entrada": int(entrada),
        "salida": int(salida), "resultado": resultado, "modelo": modelo,
    }
    if extra:
        fila.update(extra)
    try:
        append_linea(RUTA, json.dumps(fila, ensure_ascii=False))
    except OSError:
        pass


def ultimas(n: int = 200) -> list[dict]:
    return leer_lineas_json(RUTA, maximo=n)


def rendimiento(horas: int = 24) -> dict:
    from util import hoy
    corte = hoy()
    filas = [f for f in ultimas(5000) if str(f.get("fecha", "")).startswith(corte)]
    ok = sum(1 for f in filas if f.get("resultado") == "ok")
    return {
        "procesados": len(filas),
        "ok": ok,
        "fallos": len(filas) - ok,
        "segundos_totales": round(sum(float(f.get("segundos", 0)) for f in filas), 1),
        "caracteres_salida": sum(int(f.get("salida", 0)) for f in filas),
    }
