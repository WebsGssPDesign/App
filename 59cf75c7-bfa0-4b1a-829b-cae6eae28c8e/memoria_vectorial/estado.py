# -*- coding: utf-8 -*-
"""Estado del sistema. Lee del heartbeat, nunca del mtime del log."""
from __future__ import annotations

import json
import sys

import config
import heartbeat
import incidencias
import memoria
import metricas
import tablero
from util import hoy


def recoger() -> dict:
    hb = heartbeat.leer()
    notas = tablero._escanear_notas()
    indice = {}
    try:
        indice = memoria.estado()
    except Exception:
        pass
    return {
        "fecha": hoy(),
        "pipeline": {
            "activo": heartbeat.activo(),
            "paso": hb.get("paso", ""),
            "actualizado": hb.get("actualizado", ""),
            "ultimo_resultado": hb.get("resultado", ""),
            "segundos_sin_latir": round(heartbeat.segundos_sin_latir(), 1),
        },
        "incidencias": incidencias.resumen(),
        "conocimiento": {
            "notas_totales": len(notas),
            "notas_hoy": sum(1 for n in notas if n.get("fecha", "")[:10] == hoy()),
            "skills": len(tablero._contar_skills()),
            "ultima_nota": max((n.get("fecha", "") for n in notas), default=""),
        },
        "indice": indice,
        "rendimiento": metricas.rendimiento(),
        "rutas": {"boveda": str(config.VAULT), "reglas": str(config.ruta_reglas())},
    }


def imprimir(d: dict) -> None:
    p, c, i = d["pipeline"], d["conocimiento"], d["incidencias"]
    print("=" * 60)
    print(f"  Pipeline   : {'ACTIVO' if p['activo'] else 'parado'}"
          + (f"   paso={p['paso']}  ({p['actualizado']})" if p["paso"] else ""))
    print(f"  Incid.     : {i['total']} abiertas  {i['por_gravedad']}")
    print(f"  Notas      : {c['notas_totales']}  (hoy {c['notas_hoy']})   skills {c['skills']}")
    print(f"  Indice     : {d['indice']}")
    print(f"  Rendimiento: {d['rendimiento']}")
    print("=" * 60)
    for inc in i["peores"][:6]:
        print(f"   [{inc.get('gravedad')}] {inc.get('componente')}: {str(inc.get('error'))[:90]}")


def main() -> int:
    datos = recoger()
    if "--json" in sys.argv:
        print(json.dumps(datos, ensure_ascii=False, indent=2))
    else:
        imprimir(datos)
    if "--tablero" in sys.argv:
        tablero.actualizar()
        print("Tablero regenerado.")
    if "--abrir" in sys.argv:
        print(f"obsidian://open?vault={config.VAULT.name}&file=LLM-Memoria/Tablero")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
