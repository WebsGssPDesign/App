---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-infographic/references/runtime-parameters.md"
tags: [hecho]
---
# runtime-parameters.md

## Resumen
Este documento define las reglas para mapear argumentos de tiempo de ejecución en la herramienta `sn-infographic`, especificando cómo inferir automáticamente el tamaño de imagen y la relación de aspecto basándose en solicitudes del usuario o contextos implícitos, evitando interrupciones innecesarias. Su función es estandarizar los parámetros `--image-size` y `--aspect-ratio` para garantizar que las herramientas subyacentes generen imágenes con las dimensiones y proporciones correctas sin requerir confirmación constante por parte del usuario.

## Datos clave
- **Proyecto**: SenseNova Skills (`sn-infographic`).
- **Tecnologías**: Mapeo de argumentos, inferencia contextual, manejo de errores de backend.
- **Decisiones críticas**: El tamaño de imagen se infiere siempre como `2k` si no hay una declaración explícita del usuario; las palabras vagas sobre calidad (ej. "HD") se ignoran.
- **Lógica de relación de aspecto**: Se prioriza la confirmación explícita o el seguimiento del usuario; si falta, se usa la orientación (vertical/horizontal) y finalmente se infiere según el tipo de escena (ej. `9:16` para wallpapers, `4:3` para presentaciones).
- **Comandos/Parámetros**: Uso obligatorio de `--save-path` apuntando a `/tmp/openclaw/sn-infographic/<task_id>/round_<N>.png`.
- **Restricciones**: El prompt expandido se envía como `--prompt`, mientras que la relación de aspecto se infiere del `user_prompt` original.

## Etiquetas
#sn-infographic #rendering #aspect-ratio #automation

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-infographic\references\runtime-parameters.md`
