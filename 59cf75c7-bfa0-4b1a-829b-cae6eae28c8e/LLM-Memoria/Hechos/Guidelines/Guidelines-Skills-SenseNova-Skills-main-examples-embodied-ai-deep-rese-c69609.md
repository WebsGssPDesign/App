---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/examples/embodied-ai-deep-research/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este ejemplo demuestra cómo utilizar la capacidad de "investigación profunda" de SenseNova-Skills mediante un único prompt para investigar una industria y generar un informe detallado. El agente recopila automáticamente materiales públicos, los organiza por dimensiones clave (como tamaño del mercado y financiación) y emite un informe visualizado con gráficos.

## Datos clave
- **Proyecto**: Ejemplo de investigación profunda en la industria de IA encarnada (embodied AI).
- **Tecnologías**: SenseNova-Skills (`sn-deep-research`, `sn-md-to-html-report`).
- **Flujo de trabajo**:
  1. Iniciar con el prompt: "Please research the embodied AI industry and produce a professional industry research report."
  2. El agente ejecuta `sn-deep-research` para generar un informe Markdown y 5 figuras (tendencia del mercado, cuota de mercado, financiación, estructura de costos y hoja de ruta).
  3. Ejecutar `sn-md-to-html-report` para convertir el resultado en una página HTML visualizada.
- **Resultado final**: Archivo comprimido `result/具身智能行业调研.zip` conteniendo `report.html`, `report.md` y cinco imágenes de análisis (`01_market_size_trend.jpg` a `05_development_roadmap.jpg`).

## Etiquetas
#SenseNova #IAEncarnada #InvestigaciónProfunda #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\examples\embodied-ai-deep-research\README.md`
