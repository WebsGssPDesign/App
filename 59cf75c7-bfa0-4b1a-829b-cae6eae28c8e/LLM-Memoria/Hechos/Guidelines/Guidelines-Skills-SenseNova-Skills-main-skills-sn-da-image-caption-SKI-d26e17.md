---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-da-image-caption/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define una habilidad técnica para analizar imágenes y extraer datos estructurados utilizando modelos de visión. Su función principal es convertir gráficos, tablas o capturas de pantalla en descripciones textuales y luego procesar esa información para generar tablas, visualizar nuevos gráficos o exportar archivos Excel/CSV sin necesidad de configuración manual de claves API.

## Datos clave
- **Proyecto**: `sn-da-image-caption` (Skill SenseNova).
- **Script principal**: `scripts/caption.py`.
- **Modelo por defecto**: `sensenova-6.8-flash-lite`.
- **Comandos importantes**:
  - Análisis básico: `python3 scripts/caption.py /ruta/imagen.png`.
  - Prompt personalizado: `--prompt "提取所有数值，Markdown 表格格式"`.
  - Salida JSON: `--json`.
  - Procesamiento por lotes: `--batch --output archivo.json`.
- **Flujo de trabajo**: Ejecutar script -> Obtener descripción -> Parsear a DataFrame (pandas) -> Visualizar o exportar.
- **Requisito crítico**: Configuración obligatoria de fuentes chinas para matplotlib (`wqy-zenhei.ttc`) al generar gráficos nuevos.

## Etiquetas
#extracción-de-datos #visión-artificial-inteligencia #automatización-python #análisis-imágenes

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-da-image-caption\SKILL.md`
