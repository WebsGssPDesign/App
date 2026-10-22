"""Indexador de documentos para memoria vectorial.

Permite:
- Indexar archivos .md y .txt desde una carpeta.
- Buscar por similitud semántica.
- Reindexar automáticamente cambios (modo watch).

Uso:
    python indexer.py [opciones]

Opciones:
    --watch      Modo observación de cambios
    --search <q> Búsqueda rápida
    --status     Mostrar estado del índice
"""
from __future__ import annotations

import sys
import argparse
from pathlib import Path


# ------------------------------------------------------------------ importar módulos
import config
import memoria
import index


# ------------------------------------------------------------------ rutas y estado
AQUI = Path(__file__).resolve().parent


def _indexar_archivos() -> dict:
    """Indexa todos los archivos en la carpeta de bóveda.

    Returns:
        Diccionario con estadísticas del proceso.
    """
    print("Indexando archivos...")
    
    # Obtener configuración
    config.guardar_configuracion()
    
    # Crear memoria y índice
    mem = memoria.crear_memoria()
    idx = index.crear_indice()

    # Indexar archivos
    estadisticas = {
        "archivos": 0,
        "segmentos": 0,
        "errores": [],
    }

    try:
        # Buscar archivos en la bóveda
        vault_path = Path(config.vault)
        
        if not vault_path.exists():
            print(f"  ⚠️  La carpeta de bóveda no existe: {vault_path}")
            return estadisticas
        
        for ext in config.extensions.split(","):
            ext = ext.strip()
            if not ext:
                continue
            
            for archivo in vault_path.rglob(f"*.{ext}"):
                try:
                    contenido = archivo.read_text(encoding="utf-8")
                    
                    # Segmentar y agregar
                    segmentos = mem._segmentar(contenido)
                    
                    for i, segmento in enumerate(segmentos):
                        titulo = f"{archivo.stem}_{i}"
                        
                        if idx.agregar(segmento, titulo=titulo):
                            estadisticas["archivos"] += 1
                            estadisticas["segmentos"] += 1
                        
                except Exception as e:  # noqa: BLE001
                    estadisticas["errores"].append({
                        "archivo": str(archivo),
                        "error": str(e),
                    })

    except Exception as e:  # noqa: BLE001
        estadisticas["errores"].append({
            "mensaje": f"Error al indexar: {e}",
        })

    print(f"\nIndexación completada:")
    print(f"  Archivos procesados: {estadisticas['archivos']}")
    print(f"  Segmentos agregados: {estadisticas['segmentos']}")
    
    if estadisticas["errores"]:
        print(f"\n  ⚠️  Errores encontrados:")
        for err in estadisticas["errores"][:5]:  # Mostrar solo primeros 5
            if "archivo" in err:
                print(f"    - {err['archivo']}: {err.get('error', 'Desconocido')}")
            else:
                print(f"    - {err.get('mensaje', 'Desconocido')}")

    return estadisticas


def _buscar_similar(consulta: str) -> list[dict]:
    """Busca documentos similares a una consulta.

    Args:
        consulta: texto de búsqueda.

    Returns:
        Lista de resultados ordenados por relevancia.
    """
    print(f"\nBuscando para: '{consulta}'")
    
    mem = memoria.crear_memoria()
    resultados = mem.buscar_similar(consulta, top_k=10)
    
    if not resultados:
        print("  No se encontraron resultados.")
        return []
    
    print(f"  Encontrados {len(resultados)} documentos:")
    for i, r in enumerate(resultados, 1):
        print(f"\n  {i}. Relevancia: {r.get('similitud', 'N/A')}")
        print(f"     Título: {r.get('titulo', '')}")
        print(f"     Contenido: {r.get('contenido', '')[:200]}...")
    
    return resultados


def _mostrar_estado() -> dict:
    """Muestra el estado actual del sistema.

    Returns:
        Diccionario con estadísticas.
    """
    mem = memoria.crear_memoria()
    idx = index.crear_indice()

    print("\nEstado del sistema:")
    
    resultados_mem = mem.buscar("")
    resultados_idx = idx.buscar("")
    
    print(f"  Memoria: {len(resultados_mem)} documentos")
    print(f"  Índice: {len(resultados_idx)} documentos")


def _main() -> None:
    """Función principal del indexador."""
    parser = argparse.ArgumentParser(description="Indexador de memoria vectorial")
    parser.add_argument("--watch", action="store_true", help="Modo observación de cambios")
    parser.add_argument("--search", metavar="Q", help="Búsqueda rápida")
    parser.add_argument("--status", action="store_true", help="Mostrar estado del índice")
    
    args = parser.parse_args()

    if args.watch:
        print("Modo watch activado. Esperando cambios... (Ctrl+C para salir)")
        
        while True:
            try:
                # Reindexar periódicamente
                _indexar_archivos()
                
                # Esperar 5 segundos antes de la próxima revisión
                import time
                time.sleep(5)
                
            except KeyboardInterrupt:
                print("\n\nSaliendo del modo watch...")
                break

    elif args.search:
        _buscar_similar(args.search)

    elif args.status:
        _mostrar_estado()

    else:
        # Indexación normal
        _indexar_archivos()


if __name__ == "__main__":
    _main()
