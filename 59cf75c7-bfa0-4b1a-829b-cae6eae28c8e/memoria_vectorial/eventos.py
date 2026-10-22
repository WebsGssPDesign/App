# -*- coding: utf-8 -*-
"""Bus de eventos local. Append a jsonl + POST opcional a un webhook (n8n)."""
from __future__ import annotations

import json
import urllib.request

import config
from util import ahora, append_linea, leer_lineas_json

RUTA = config.SISTEMA / "eventos.jsonl"


def emitir(tipo: str, datos: dict | None = None, webhook: bool = True) -> None:
    fila = {"fecha": ahora(), "tipo": tipo}
    fila.update(datos or {})
    try:
        append_linea(RUTA, json.dumps(fila, ensure_ascii=False))
    except OSError:
        pass
    if not webhook or not config.get("eventos.activo", True):
        return
    url = str(config.get("eventos.webhook", "") or "")
    if not url:
        return
    try:
        req = urllib.request.Request(
            url, data=json.dumps(fila, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=float(config.get("eventos.timeout", 5))) as r:
            r.read(1)
    except Exception:
        pass


def ultimos(n: int = 50) -> list[dict]:
    return leer_lineas_json(RUTA, maximo=n)
