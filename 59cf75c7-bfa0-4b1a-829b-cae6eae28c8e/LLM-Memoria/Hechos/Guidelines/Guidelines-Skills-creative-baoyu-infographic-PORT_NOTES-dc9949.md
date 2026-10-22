---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/baoyu-infographic/PORT_NOTES.md"
tags: [hecho]
---
# PORT_NOTES.md

## Resumen
Este archivo documenta la adaptación del proyecto `baoyu-infographic` para integrarse en la infraestructura de Hermes, detallando las modificaciones específicas realizadas sobre el código fuente original. Su función es servir como guía técnica para entender cómo se han ajustado los comandos, herramientas y flujos de trabajo originales para operar dentro del nuevo entorno.

## Datos clave
- **Proyecto**: Adaptación de `baoyu-infographic` (v1.56.1) desde el repositorio upstream de JimLiu.
- **Cambios principales en SKILL.md**: El namespace cambió de `openclaw` a `hermes`; el disparador pasó del comando `/baoyu-infographic` a coincidencia de lenguaje natural; la generación de imágenes ahora usa la herramienta `image_generate`.
- **Restricciones de plataforma**: Soporte limitado exclusivamente a Linux y macOS, eliminando soporte para Windows/WSL.
- **Operaciones de archivo**: Se reemplazaron comandos Bash por herramientas nativas de Hermes (`write_file`, `read_file`).
- **Sincronización**: Los archivos de referencia se pueden sobrescribir directamente, pero `SKILL.md` requiere fusión manual debido a las adaptaciones locales.

## Etiquetas
#baoyu-infographic #hermes #adaptación-de-código #documentación-técnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\baoyu-infographic\PORT_NOTES.md`
