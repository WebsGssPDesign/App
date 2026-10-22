---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-standard/references/box-agent-tool-contract.md"
tags: [hecho]
---
# box-agent-tool-contract.md

## Resumen
Este documento define el contrato técnico para adaptar la habilidad `sn-ppt-standard` al entorno Box-Agent, estableciendo reglas estrictas para la ejecución de scripts, la delegación de tareas y el flujo de trabajo entre agentes padre e hijos. Su objetivo es garantizar que las operaciones de renderizado, generación de imágenes y gestión de archivos se realicen con seguridad absoluta, evitando dependencias del directorio actual y asegurando un registro preciso de los activos generados o descargados.

## Datos clave
- **Proyecto**: Adaptación de `sn-ppt-standard` para Box-Agent.
- **Rutas críticas**: Uso obligatorio de `$DECK_DIR` como raíz absoluta; prohibido usar `.` o rutas relativas no resueltas.
- **Comandos y scripts**: Ejecución de `deck.py`, `render.py`, `serper_images.py` por el padre; uso de `bash(command, timeout)` en lugar de parámetros antiguos de trabajo.
- **Mapeo de herramientas**: Traducción de `patch` a `edit_file`, delegación vía `sub_agent` con `write_scope` preciso, y generación de imágenes con `watermark=false`.
- **Flujo de renderizado**: Ciclo estricto: sub-agente escribe HTML -> padre ejecuta `render.py --batch` -> inspección nativa (`strategy="native"`) -> corrección si es necesario.
- **Gestión de activos**: Registro automático de origen (generado o descargado) mediante `deck.py asset-register`; claves API solo desde variables de entorno.

## Etiquetas
#box-agent #sn-ppt-standard #contrato-técnico #renderizado

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-standard\references\box-agent-tool-contract.md`
