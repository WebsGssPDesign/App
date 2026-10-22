---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Software_regression"
tema: "Git Hooks"
tags: [web]
---
# Software regression

## Resumen
Una regresión de software ocurre cuando un cambio en el código o el entorno hace que una funcionalidad previamente operativa deje de funcionar correctamente o degrade su rendimiento. Para mitigar este problema, se emplean técnicas como pruebas de regresión automatizadas y análisis de impacto antes de realizar los cambios en el repositorio.

## Datos clave
- **Tipos:** Local (error en el módulo modificado), Remota (error afecta otros módulos) y Unmascarada (revela un error preexistente).
- **Prevención:** Pruebas unitarias e integrales, Git Hooks para ejecutar scripts antes del commit, análisis de impacto y linters.
- **Detección:** Comparación de métricas de rendimiento y uso de recursos con estadística significativa.
- **Localización:** Bisección binaria (busca de commits entre un estado bueno y uno malo), perfiles de llamadas ("call trees") y análisis de flujo de datos incremental.

## Etiquetas
#calidad_de_software #pruebas_de_regresión #desarrollo_agil #depuración

Fuente: https://en.wikipedia.org/wiki/Software_regression
