# -*- coding: utf-8 -*-
"""Registro de incidencias. Multi-escritor: lock + escritura atomica.

Estados: abierta -> reintentando -> aislada -> resuelta
"""
from __future__ import annotations

from pathlib import Path

import config
from util import ahora, atomic_write_json, bloqueo, leer_json

RUTA = config.SISTEMA / "incidencias.json"
LOCK = config.SISTEMA / ".incidencias.lock"
GRAVEDADES = ("info", "baja", "media", "alta", "critica")


def _cargar() -> dict:
    datos = leer_json(RUTA, {"version": 1, "abiertas": [], "cerradas": [], "fuentes": {}})
    datos.setdefault("abiertas", [])
    datos.setdefault("cerradas", [])
    datos.setdefault("fuentes", {})
    return datos


def gravedad_orden(g: str) -> int:
    try:
        return GRAVEDADES.index(g)
    except ValueError:
        return 2


def registrar(componente: str, error: str, gravedad: str = "media",
              detalle: str = "") -> dict | None:
    """Si ya hay una incidencia abierta con el mismo componente+error, suma un reintento."""
    if gravedad not in GRAVEDADES:
        gravedad = "media"
    with bloqueo(LOCK, vencimiento=30) as mio:
        if not mio:
            return None
        datos = _cargar()
        clave = f"{componente}|{error[:120]}"
        for inc in datos["abiertas"]:
            if inc.get("clave") == clave:
                inc["reintentos"] = int(inc.get("reintentos", 1)) + 1
                inc["actualizado"] = ahora()
                inc["estado"] = "reintentando" if inc["reintentos"] > 1 else inc["estado"]
                if gravedad_orden(gravedad) > gravedad_orden(inc.get("gravedad", "media")):
                    inc["gravedad"] = gravedad
                if detalle:
                    inc["detalle"] = detalle[:500]
                atomic_write_json(RUTA, datos)
                return inc
        nueva = {
            "id": f"INC-{len(datos['abiertas']) + len(datos['cerradas']) + 1:05d}",
            "clave": clave, "fecha": ahora(), "componente": componente,
            "error": error[:300], "detalle": detalle[:500], "gravedad": gravedad,
            "reintentos": 1, "estado": "abierta", "actualizado": ahora(),
        }
        datos["abiertas"].append(nueva)
        atomic_write_json(RUTA, datos)
        return nueva


def registrar_si_toca(componente: str, error: str, gravedad: str = "media",
                      detalle: str = "", cooldown_min: int = 15) -> dict | None:
    """Como registrar(), pero no suma reintento si la ultima vez fue hace menos de cooldown_min."""
    from datetime import datetime
    for inc in abiertas(componente):
        if error[:120] in inc.get("clave", ""):
            try:
                ultima = datetime.strptime(inc.get("actualizado", ""), "%Y-%m-%d %H:%M:%S")
                if (datetime.now() - ultima).total_seconds() < cooldown_min * 60:
                    return inc
            except ValueError:
                pass
    return registrar(componente, error, gravedad, detalle)


def cerrar(componente: str, error: str = "", nota: str = "") -> bool:
    with bloqueo(LOCK, vencimiento=30) as mio:
        if not mio:
            return False
        datos = _cargar()
        movidas = []
        for inc in list(datos["abiertas"]):
            if inc.get("componente") != componente:
                continue
            if error and error[:120] not in inc.get("clave", ""):
                continue
            inc.update({"estado": "resuelta", "cerrada": ahora(), "nota": nota[:300]})
            datos["abiertas"].remove(inc)
            movidas.append(inc)
        if not movidas:
            return False
        datos["cerradas"] = (datos["cerradas"] + movidas)[-500:]
        atomic_write_json(RUTA, datos)
        return True


def aislar(componente: str, motivo: str, horas: int = 24) -> None:
    from datetime import datetime, timedelta
    with bloqueo(LOCK, vencimiento=30) as mio:
        if not mio:
            return
        datos = _cargar()
        hasta = (datetime.now() + timedelta(hours=horas)).strftime("%Y-%m-%d %H:%M:%S")
        for inc in datos["abiertas"]:
            if inc.get("componente") == componente:
                inc.update({"estado": "aislada", "hasta": hasta, "nota": motivo[:300],
                            "actualizado": ahora()})
        atomic_write_json(RUTA, datos)


def aislada_vigente(componente: str) -> bool:
    from datetime import datetime
    for inc in abiertas(componente):
        if inc.get("estado") != "aislada":
            continue
        try:
            if datetime.now() < datetime.strptime(inc.get("hasta", ""), "%Y-%m-%d %H:%M:%S"):
                return True
        except ValueError:
            return True
    return False


esta_aislada = aislada_vigente


def abiertas(componente: str = "") -> list[dict]:
    lista = _cargar()["abiertas"]
    return [i for i in lista if not componente or i.get("componente") == componente]


def fallos_de(componente: str) -> int:
    return sum(int(i.get("reintentos", 1)) for i in abiertas(componente))


def resumen() -> dict:
    lista = abiertas()
    return {
        "total": len(lista),
        "por_gravedad": {g: sum(1 for i in lista if i.get("gravedad") == g) for g in GRAVEDADES},
        "peores": sorted(lista, key=lambda i: (-gravedad_orden(i.get("gravedad", "media")),
                                               i.get("fecha", "")))[:10],
    }
