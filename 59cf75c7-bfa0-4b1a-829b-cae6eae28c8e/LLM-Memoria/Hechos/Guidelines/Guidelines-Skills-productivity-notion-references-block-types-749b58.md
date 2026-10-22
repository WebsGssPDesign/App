---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/notion/references/block-types.md"
tags: [hecho]
---
# block-types.md

## Resumen
Este documento sirve como referencia técnica para interactuar con los tipos de bloques de Notion mediante su API, detallando cómo construirlos y leer sus datos. Proporciona ejemplos de JSON para crear elementos como párrafos, listas y código, además de una tabla que indica dónde extraer el texto al consultar páginas existentes.

## Datos clave
- **Endpoint de creación**: `PATCH /v1/blocks/{page_id}/children` con un array `children`.
- **Estructura JSON**: Cada bloque requiere `"object": "block"` y un campo específico según el tipo (ej. `"paragraph"`, `"heading_1"`).
- **Tipos soportados**: Párrafos, encabezados (H1-H3), listas (viñetas/numéricas), casillas de verificación, citas, notas destacadas, código, acordeones, separadores, marcadores web e imágenes.
- **Endpoint de lectura**: `GET /v1/blocks/{page_id}/children`.
- **Extracción de texto**: Se accede principalmente al campo `.rich_text` dentro del objeto específico del tipo; para bloques como `to_do`, también se verifica el estado booleano en `.checked`.

## Etiquetas
#Notion #API #Desarrollo #Documentación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\notion\references\block-types.md`
