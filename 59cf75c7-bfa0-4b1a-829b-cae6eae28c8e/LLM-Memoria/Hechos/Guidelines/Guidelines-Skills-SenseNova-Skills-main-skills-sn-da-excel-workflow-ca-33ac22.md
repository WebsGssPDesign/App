---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-excel-workflow/capability/excel-data-filtering/condition-filtering/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento detalla una sub-habilidad para filtrar datos en Excel basándose en condiciones específicas y optimizar el manejo de archivos grandes. Sirve como guía paso a paso para limpiar datos, aplicar filtros complejos (como colores RGB o expresiones regulares) y exportar resultados con estilos visuales destacados.

## Datos clave
- **Proyecto**: SenseNova-Skills (flujo de trabajo de análisis Excel).
- **Tecnologías**: Python, Pandas (`pd`), OpenPyXL.
- **Decisiones lógicas**: Selección dinámica de columnas ('域名', '缩写', etc.) y uso de `errors='coerce'` para convertir datos sucios a numéricos sin fallar el script.
- **Filtros específicos**: Combinación de canales RGB (`Red==0 & Green==0...`), prefijos de strings (`startswith('TXL3')`) y patrones regulares (`--pct-`).
- **Pasos de exportación**: Guardado en `filtered_result.xlsx` con hojas separadas ('统计结果', '正则提取') y aplicación de relleno rojo a todas las filas (excepto cabeceras) para resaltar resultados.

## Etiquetas
#Python #Pandas #ExcelAutomation #DataCleaning

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-excel-workflow\capability\excel-data-filtering\condition-filtering\SKILL.md`
