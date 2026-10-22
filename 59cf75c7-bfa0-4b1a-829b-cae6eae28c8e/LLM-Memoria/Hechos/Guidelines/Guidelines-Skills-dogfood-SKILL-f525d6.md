---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/dogfood/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define un flujo de trabajo sistemático para realizar pruebas exploratorias de calidad (QA) en aplicaciones web, permitiendo identificar errores, recopilar evidencia visual y generar informes estructurados. El proceso está diseñado para ejecutarse en múltiples plataformas utilizando una suite de herramientas de navegador automatizadas que combinan navegación manual con análisis por IA.

## Datos clave
- **Proyecto**: Dogfood (Exploratory QA).
- **Tecnologías**: Herramientas de navegador (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_vision`, `browser_console`).
- **Flujo de trabajo**: 5 fases: Planificar, Explorar, Recopilar Evidencia, Categorizar y Generar Informe.
- **Pasos críticos**: Verificar consola (`browser_console`) tras cada navegación e interacción; usar `annotate=true` en capturas para etiquetar elementos interactivos.
- **Salida**: Directorio con carpetas de capturas y un archivo `report.md` con resumen ejecutivo, tabla de incidencias y detalles técnicos.

## Etiquetas
#QA #PruebasWeb #Automatización #Dogfood

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\dogfood\SKILL.md`
