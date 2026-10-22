---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un flujo de trabajo automatizado para el análisis de datos en Excel, diseñado para manejar desde archivos pequeños hasta grandes volúmenes de información sin colapsar la memoria. Su función principal es orquestar una serie de capacidades subyacentes que cubren todo el ciclo: lectura inteligente, detección de tamaño, limpieza de datos, filtrado y exportación de resultados formateados.

## Datos clave
- **Proyecto**: `sn-da-excel-workflow` (SenseNova).
- **Tecnologías**: Python (`pandas`, `openpyxl`, `matplotlib`), Parquet para caché eficiente.
- **Regla crítica de escalabilidad**: Si el archivo tiene ≥10k filas, usar Parquet; si tiene ≥100k filas, obligatoriamente cargar la habilidad `sn-da-large-file-analysis` y evitar `pd.read_excel()`.
- **Pasos del flujo**: 1. Contar filas (modo `read_only`). 2. Gate de tamaño. 3. Inspección de esquema (muestra pequeña). 4. Limpieza (valores nulos, texto CJK). 5. Filtrado y agregación. 6. Exporto a Excel/CSV con enlace de descarga.
- **Configuración obligatoria**: Bloque de código para configurar fuentes de caracteres chinos (`SimHei.ttf`) en gráficos de `matplotlib`.

## Etiquetas
#análisis-de-datos #excel-python #optimización-memoria #limpieza-de-datos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\SKILL.md`
