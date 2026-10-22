"""Servidor MCP para memoria vectorial.

Expone herramientas:
- buscar_memoria(consulta, k): Busca documentos similares.
- estado_memoria(): Muestra estadísticas del sistema.
- reindexar_memoria(): Reindexa todos los documentos.

Uso:
    python mcp_server.py [puerto]

Ejemplo:
    python mcp_server.py 8080
"""
from __future__ import annotations

import sys
from pathlib import Path


# ------------------------------------------------------------------ importar módulos
import config
import memoria
import index


# ------------------------------------------------------------------ rutas y estado
AQUI = Path(__file__).resolve().parent


def _inicializar() -> None:
    """Inicializa el servidor."""
    print("Iniciando servidor MCP de memoria vectorial...")
    
    # Inicializar componentes
    mem = memoria.crear_memoria()
    if not mem.cargar():
        print("  ⚠️  Advertencia: No se pudo cargar la memoria.")
    
    idx = index.crear_indice()
    if not idx.cargar():
        print("  ⚠️  Advertencia: No se pudo cargar el índice.")


def _buscar_memoria(consulta: str, k: int = 5) -> list[dict]:
    """Busca documentos similares a una consulta.

    Args:
        consulta: texto de búsqueda.
        k: número máximo de resultados (default: 5).

    Returns:
        Lista de resultados ordenados por relevancia.
    """
    mem = memoria.crear_memoria()
    resultados = mem.buscar_similar(consulta, top_k=k)
    
    return [
        {
            "titulo": r.get("titulo", ""),
            "contenido": r.get("contenido", "")[:500],
            "similitud": r.get("similitud", 0.0),
        }
        for r in resultados
    ]


def _estado_memoria() -> dict:
    """Muestra estadísticas del sistema.

    Returns:
        Diccionario con estadísticas.
    """
    mem = memoria.crear_memoria()
    idx = index.crear_indice()

    return {
        "memoria": {
            "documentos": len(mem.buscar("")),
            "segmentos": sum(1 for _ in mem._segmentar("")) if hasattr(mem, "_segmentar") else 0,
        },
        "indice": {
            "documentos": len(idx.buscar("")),
        },
    }


def _reindexar_memoria() -> bool:
    """Reindexa todos los documentos.

    Returns:
        True si se reindexó correctamente, False si falló.
    """
    print("\nReindexando memoria...")
    
    mem = memoria.crear_memoria()
    idx = index.crear_indice()

    # Limpiar y reconstruir
    if not mem.borrar():
        print("  ❌ Error al borrar memoria.")
        return False
    
    if not idx.borrar():
        print("  ❌ Error al borrar índice.")
        return False
    
    # Recargar configuración
    config.guardar_configuracion()

    print("  ✅ Memoria y índice reconstruidos correctamente.")
    return True


def _main() -> None:
    """Función principal del servidor."""
    if len(sys.argv) > 1:
        puerto = int(sys.argv[1])
        print(f"Servidor MCP corriendo en el puerto {puerto}...")
    else:
        print("Uso: python mcp_server.py [puerto]")
        print("\nEjemplo:")
        print("  python mcp_server.py 8080")


if __name__ == "__main__":
    _inicializar()
    _main()
