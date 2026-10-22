---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-non-spreadsheet-analysis/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un flujo de trabajo para analizar y extraer datos estructurados (tablas, gráficos, texto) de archivos Word, PDF y PowerPoint. Su objetivo es garantizar una extracción completa y verificada evitando errores comunes como detenerse en el primer archivo o ignorar imágenes sin texto.

## Datos clave
- **Rutas**: `/mnt/data/...` para entrada; sub-habilidades en `capability/{word,pdf,ppt}-analysis/SKILL.md`.
- **Comandos/Pasos**: Detectar si la entrada es directorio (procesar todos los archivos) o archivo único; cargar solo el subskill correspondiente al formato.
- **Reglas críticas**: Iterar todas las páginas/diapositivas; usar `caption.py` para imágenes/gráficos en lugar de OCR directo (`pytesseract`); verificar cálculos mostrando valores intermedios y unidades.
- **Exclusiones**: No usar para análisis de Excel/CSV ni para imágenes puras sin contexto documental.

## Etiquetas
#análisis-documental #extracción-datos #automatización-python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-non-spreadsheet-analysis\SKILL.md`
