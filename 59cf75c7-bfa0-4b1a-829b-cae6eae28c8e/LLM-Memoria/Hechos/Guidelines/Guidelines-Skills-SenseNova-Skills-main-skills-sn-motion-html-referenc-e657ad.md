---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-motion-html/references/frontend.md"
tags: [hecho]
---
# frontend.md

## Resumen
Este documento define la arquitectura frontend para una experiencia de video continua, estructurada como un único plano virtual sin cortes abruptos. Su objetivo es garantizar una navegación fluida entre escenas y conectores mediante renderizado absoluto y gestión avanzada del progreso global. Además, establece pautas estrictas para la accesibilidad, el diseño responsivo y la seguridad al servir los archivos generados.

## Datos clave
- **Estructura**: Secuencia lineal de `scene` → `connector` sin tarjetas independientes ni bloques pegajosos.
- **Renderizado**: Uso de Blob URLs para clips cercanos y crossfading en uniones de cuadros coincidentes.
- **Presets UI**: Tres modos (`folio`, `caption`, `graphic`) que modifican solo el encabezado y la composición, manteniendo la topología del video intacta.
- **Ubicación de texto**: Posiciones fijas por escena (`left`, `right`, `bottom`, `center`); ocultar copias durante conectores en lugar de rotar párrafos.
- **Accesibilidad**: Panel inferior por defecto en pantallas estrechas, cultivo seguro del sujeto y priming de videos mudos para móviles.
- **Seguridad**: Denegación explícita de archivos `.env` y uso de `scripts/serve_project.py` para previsualizaciones locales seguras.

## Etiquetas
#frontend #video-streaming #accessibility #ui-design #hosting-safety

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-motion-html\references\frontend.md`
