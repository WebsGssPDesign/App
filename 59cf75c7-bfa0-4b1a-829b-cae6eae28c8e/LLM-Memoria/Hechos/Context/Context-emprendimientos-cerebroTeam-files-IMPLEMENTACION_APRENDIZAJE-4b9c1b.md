---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/files/IMPLEMENTACION_APRENDIZAJE.md"
tags: [hecho]
---
# IMPLEMENTACION_APRENDIZAJE.md

## Resumen
Este documento describe la implementación y uso de un sistema de aprendizaje autónomo que integra ChromaDB para almacenar conocimiento. Permite a una IA buscar temas en internet, procesarlos localmente y guardarlos como base de datos vectorial para consultas futuras más precisas. Sirve tanto para ejecución en background continuo como para integración en aplicaciones web mediante FastAPI.

## Datos clave
- **Proyecto**: Sistema de Aprendizaje Autónomo con ChromaDB (cerebroTeam).
- **Tecnologías**: Python, ChromaDB, DuckDuckGo, Wikipedia, IA local, FastAPI, Threading.
- **Archivos principales**: `sistema_completo.py` (orquestación), `aprendizaje_autonomo_prod.py`, `knowledge_base_prod.py`.
- **Flujo de aprendizaje**: Selección de temas -> Búsqueda web -> Procesamiento con IA -> Guardado en ChromaDB.
- **Comandos/Pasos clave**: `sistema.aprender(num_temas=5)`, `sistema.consultar(pregunta, usar_kb=True)`, `sistema.buscar_conocimiento()`.
- **Integración Web**: Endpoints `/aprender` y `/consultar` en FastAPI.
- **Configuración**: Posibilidad de cambiar ruta de ChromaDB (`F:/mi_proyecto/base_de_datos`) y modelo de IA en `ia_con_kb.py`.

## Etiquetas
#ChromaDB #AprendizajeAutonomo #IA #Python #FastAPI

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\files\IMPLEMENTACION_APRENDIZAJE.md`
