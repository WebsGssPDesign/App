---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/webs/landing/AGENTS.md"
tags: [hecho]
---
# AGENTS.md

## Resumen
Este archivo actúa como una advertencia técnica para desarrolladores que trabajan con Next.js, indicando que la versión instalada contiene cambios rupturas respecto a los datos de entrenamiento comunes. Su función es obligar al equipo a consultar la documentación interna específica antes de escribir código y recuerda que el bloque se regenera automáticamente durante el desarrollo.

## Datos clave
- **Proyecto**: Entorno de desarrollo Next.js con cambios en APIs, convenciones y estructura de archivos.
- **Tecnologías**: Next.js (versión actualizada), Node.js.
- **Decisiones**: Se debe verificar la documentación en `node_modules/next/dist/docs/` antes de programar.
- **Rutas**: El bloque se genera desde `node_modules/next/dist/server/lib/generate-agent-files.js`.
- **Pasos importantes**: No eliminar el bloque manualmente; si se quita del diff, se recreará al ejecutar `next dev`.

## Etiquetas
#NextJS #DesarrolloFrontend #DocumentaciónTécnica #CambiosRupturas

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\webs\landing\AGENTS.md`
