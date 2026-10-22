---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/venv_proyecto/Lib/site-packages/chromadb/utils/embedding_functions/schemas/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este directorio alberga esquemas JSON que definen la configuración de funciones de incrustación (embedding) en ChromaDB para garantizar compatibilidad entre lenguajes y validar cambios. Su propósito es asegurar que las configuraciones sean estrictas, consistentes y evolucionen de manera controlada mediante un sistema de versionado.

## Datos clave
- **Proyecto**: ChromaDB (librería de vectores).
- **Tecnologías**: JSON Schema Draft-07, Python (`chromadb.utils.embedding_functions.schemas`).
- **Estructura del esquema**: Incluye `version`, `title`, `description`, `properties`, `required` y `additionalProperties` (siempre falso).
- **Función de validación**: `validate_config(config, "nombre_funcion")`.
- **Pasos para agregar esquemas**: Crear archivo JSON con nombre de la función, definir esquema Draft-07 y actualizar la función correspondiente.
- **Gestión de versiones**: Incrementar el número de versión al modificar un esquema para mantener compatibilidad hacia atrás.

## Etiquetas
#ChromaDB #Embeddings #JSONSchema #Validación #Configuración

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\venv_proyecto\Lib\site-packages\chromadb\utils\embedding_functions\schemas\README.md`
