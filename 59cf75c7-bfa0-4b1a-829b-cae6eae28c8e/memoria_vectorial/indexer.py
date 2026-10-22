# -*- coding: utf-8 -*-
"""CLI del indice: sync, watch, busqueda y evaluacion de umbrales.

Reconstruido el 2026-10-22 segun PARCHES/indexer.py.md (secciones 1-3) sobre la
API real de memoria.py (connect/embed/sync/search/indexar_archivo/estado/parado).
El modulo `index` que importaban las versiones corruptas NO existe: todo pasa
por `memoria`.

Uso:
    python indexer.py                 -> sincroniza una vez
    python indexer.py --watch 20      -> vigila cada 20 s (STOP_INDEXER para salir)
    python indexer.py --search "texto" [--k 5] [--ambito todo|mios|web]
    python indexer.py --eval Sistema/eval.json [--k 5]   -> calibra MIN_SIM
    python indexer.py --forzar        -> reconstruye el indice desde cero
    python indexer.py --check         -> delega en config.py --check
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import incidencias
import memoria
import tablero


def _print_sync(r: dict) -> None:
    if not r:
        return
    if r.get("omitido"):
        print(f"[sync] omitido: {r['omitido']}")
        return
    print(f"[sync] nuevos={r.get('nuevos', 0)} modificados={r.get('modificados', 0)} "
          f"eliminados={r.get('eliminados', 0)} sin_cambios={r.get('sin_cambios', 0)}"
          + (" (parcial)" if r.get("parcial") else ""))


def evaluar(ruta_json: str | Path, k: int = 5) -> int:
    """PARCHES §2: prueba umbrales de 0.25 a 0.65 y reporta recall y precision.

    Formato esperado (lista de {"consulta": str, "esperado": subcadena_de_ruta}):
        [{"consulta": "como configuro el lock de sqlite", "esperado": "memoria"}]
    Nota: usa auto_sync=False para medir solo el indice ya construido.
    """
    ruta = Path(ruta_json)
    try:
        casos = json.loads(ruta.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"[eval] no puedo leer {ruta}: {e}")
        return 1
    if not isinstance(casos, list) or not casos:
        print("[eval] el JSON debe ser una lista no vacia de casos")
        return 1

    # Precarga una vez (los resultados se re-filtran por umbral sin re-embeber).
    crudo: list[list[dict]] = []
    for c in casos:
        consulta = str(c.get("consulta", "")).strip()
        esperado = str(c.get("esperado", "")).lower()
        res = memoria.search(consulta, k=max(int(k), 1), auto_sync=False)
        crudo.append([({"caso": esperado, **r}) for r in res])

    print(f"[eval] {len(casos)} consultas, k={k}. Umbrales de 0.25 a 0.65:")
    print("  umbral   recall   precision   aciertos/total")
    mejor_umbral, mejor_f1 = 0.0, -1.0
    umbral_base = float(memoria.MIN_SIM)
    for u in [round(0.25 + 0.05 * i, 2) for i in range(9)]:
        tp = fp = fn = 0
        for caso_res in crudo:
            filtrados = [r for r in caso_res if float(r.get("score", 0)) >= u]
            acierto = any(esperado in str(r["ruta"]).lower() for r in filtrados)
            relevantes = sum(1 for r in filtrados
                             if r["caso"] and r["caso"] in str(r["ruta"]).lower())
            tp += relevantes if acierto else 0
            fp += len(filtrados) - relevantes
            fn += 0 if acierto else 1
        recall = tp / (tp + fn) if (tp + fn) else 1.0
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        f1 = (2 * recall * precision / (recall + precision)) if (recall + precision) else 0.0
        marca = ""
        if abs(u - umbral_base) < 1e-9:
            marca = "  <- MIN_SIM actual"
        if f1 > mejor_f1:
            mejor_f1, mejor_umbral = f1, u
            marca += "  *"
        print(f"  {u:.2f}     {recall:.2f}      {precision:.2f}"
              f"        {tp}/{tp + fn}{marca}")
    print(f"[eval] mejor F1={mejor_f1:.2f} en umbral {mejor_umbral:.2f}. "
          f"Si convence, ponlo en Sistema/reglas.json -> memoria.min_sim.")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)

    # PARCHES §3: --check delega en config.
    if "--check" in argv:
        import config
        return config.main(["--check"])

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--watch", type=int, default=0, metavar="SEG",
                        help="vigila la boveda cada SEG segundos hasta crear STOP_INDEXER")
    parser.add_argument("--search", type=str, default="", help="busqueda puntual")
    parser.add_argument("--k", type=int, default=5, help="resultados de busqueda/eval")
    parser.add_argument("--ambito", type=str, default="todo",
                        choices=["todo", "mios", "web"], help="filtro de busqueda")
    parser.add_argument("--eval", type=str, default="", metavar="JSON",
                        help="calibra MIN_SIM con un set de consultas esperadas")
    parser.add_argument("--forzar", action="store_true",
                        help="reconstruye el indice desde cero")
    args = parser.parse_args(argv)

    if args.eval:
        return evaluar(args.eval, args.k)

    if args.search:
        res = memoria.search(args.search, k=args.k, ambito=args.ambito)
        print(memoria.formatear(res))
        return 0

    # PARCHES §1: --watch con parada limpia.
    if args.watch:
        parar_idx = memoria.STOP_PATH.with_name("STOP_INDEXER")
        print(f"[watch] vigilando cada {args.watch}s. Crea {parar_idx.name} para salir.")
        while not memoria.parado():
            try:
                r = memoria.sync()
            except Exception as e:
                incidencias.registrar("indice", type(e).__name__, "media", str(e)[:200])
                r = {}
            if r and any(r.get(k) for k in ("nuevos", "modificados", "eliminados")):
                print(f"[watch] +{r.get('nuevos', 0)} ~{r.get('modificados', 0)} -{r.get('eliminados', 0)}"
                      + (" (parcial)" if r.get("parcial") else ""))
                tablero.actualizar_si_toca()
            time.sleep(args.watch)
        print("[watch] salida limpia.")
        return 0

    # Sync unico (por defecto o con --forzar).
    t0 = time.time()
    try:
        r = memoria.sync(forzar=args.forzar)
    except Exception as e:
        incidencias.registrar("indice", type(e).__name__, "media", str(e)[:200])
        print(f"[sync] error: {type(e).__name__}: {str(e)[:200]}")
        return 1
    _print_sync(r)
    if r and any(r.get(k) for k in ("nuevos", "modificados", "eliminados")):
        tablero.actualizar_si_toca()
    print(f"[sync] terminado en {time.time() - t0:.1f}s. estado={memoria.estado()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
