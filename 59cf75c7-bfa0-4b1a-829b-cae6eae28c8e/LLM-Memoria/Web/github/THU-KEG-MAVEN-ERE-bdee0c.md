---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/THU-KEG/MAVEN-ERE"
tema: "Temporal Event Sourcing"
tags: [web]
---
# THU-KEG/MAVEN-ERE

## Resumen
MAVEN-ERE es el primer conjunto de datos unificado y a gran escala diseñado para la extracción de relaciones entre eventos, abarcando referencia coreferencial, temporal, causal y de subeventos. El repositorio proporciona tanto el código fuente como los archivos de entrenamiento y validación en formato JSONL, listos para su uso en investigación.

## Datos clave
- **Escala:** 4.480 documentos con más de 103 mil cadenas coreferenciales y cerca de 58 mil relaciones causales.
- **Relaciones temporales:** BEFORE, OVERLAP, CONTAINS, SIMULTANEOUS, BEGINS-ON, ENDS-ON.
- **Relaciones causales:** CAUSE, PRECONDITION.
- **Formato:** Archivos `.jsonl` que incluyen tokens, oraciones, eventos (con palabras detonadoras), expresiones temporales (TIMEX) y matrices de relaciones.
- **Instalación:** `pip install -r requirements.txt`.
- **Descarga:** Disponible vía Tsinghua Cloud o Google Drive; el conjunto de prueba requiere envío a CodaLab para evitar filtraciones.

## Etiquetas
#procesamiento-del-lenguaje-natural #extracción-de-eventos #datasets #NLP #MAVEN-ERE

Fuente: https://github.com/THU-KEG/MAVEN-ERE
