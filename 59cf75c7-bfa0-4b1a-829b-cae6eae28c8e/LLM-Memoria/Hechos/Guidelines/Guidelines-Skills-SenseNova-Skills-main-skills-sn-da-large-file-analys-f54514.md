---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-large-file-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un motor de análisis de alto rendimiento para conjuntos de datos en Excel con más de 10.000 filas, evitando la saturación de memoria mediante lectura streaming y conversión a Parquet. Su función es garantizar la estabilidad del sistema al manejar archivos masivos o cuando se detectan términos relacionados con grandes volúmenes de datos.

## Datos clave
- **Proyecto**: sn-da-large-file-analysis (Skill para análisis de Excel).
- **Límite crítico**: Se activa obligatoriamente si las filas totales son ≥ 10,000.
- **Estrategias por escala**:
    - < 10k: `pd.read_excel()` directo.
    - 10k–100k: Leer Excel → Convertir a Parquet → Analizar con Parquet.
    - > 100k: Usar `openpyxl` en modo `read_only` + `iter_rows` para streaming hacia Parquet.
- **Optimizaciones**: Desactivar `df.iterrows()` y `df.apply`; usar `itertuples()` o operaciones vectorizadas; gestión de memoria con `gc.collect()`.
- **Configuración de fuentes**: Bloque fijo de rutas para fuentes CJK (SimHei) sin búsqueda dinámica.
- **Funciones principales**: `inspect_excel` (inspección sin carga), `stream_excel_to_parquet` (lectura chunked), `convert_excel_to_parquet`.

## Etiquetas
#análisis_de_datos #excel_masivo #optimización_python #parquet

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-large-file-analysis\SKILL.md`
