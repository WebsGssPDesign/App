---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/dogfood/references/issue-taxonomy.md"
tags: [hecho]
---
# issue-taxonomy.md

## Resumen
Este documento define una taxonomía estandarizada para clasificar errores detectados durante pruebas de calidad (QA) internas. Su objetivo es facilitar la priorización y gestión de incidencias, diferenciando entre fallos críticos que bloquean el sistema y problemas menores de pulido o experiencia de usuario.

## Datos clave
- **Niveles de severidad**: Critical (bloqueo total/pérdida de datos), High (impide funcionalidad con workaround), Medium (afecta UX pero no bloques), Low (polish, ortografía).
- **Categorías funcionales**: Functional (flujos rotos), Visual (layout, imágenes), Accessibility (WCAG, navegación teclado), Console (errores JS, CORS), UX (confusión, falta de feedback), Content (textos, enlaces muertos).
- **Ejemplos específicos**: Autenticación rota, formularios que pierden datos, contrastes de color insuficientes, contenido "Lorem ipsum" en producción.

## Etiquetas
#QA #Taxonomía #GestiónDeErrores #DogfoodTesting

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\dogfood\references\issue-taxonomy.md`
