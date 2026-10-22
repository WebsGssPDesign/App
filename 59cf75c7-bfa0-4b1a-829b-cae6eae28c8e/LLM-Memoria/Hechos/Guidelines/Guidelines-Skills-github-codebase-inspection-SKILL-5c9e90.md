---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/github/codebase-inspection/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía detalla cómo analizar repositorios de código utilizando la herramienta `pygount` para obtener métricas como líneas de código (LOC), distribución por lenguaje y proporción de comentarios. Su objetivo principal es ayudar a los usuarios a evaluar rápidamente el tamaño, la composición y la salud técnica de un proyecto sin necesidad de inspección manual exhaustiva.

## Datos clave
- **Herramienta**: `pygount` (instalación vía pip).
- **Comando esencial**: Siempre usar `--folders-to-skip` para excluir directorios como `.git`, `node_modules` y entornos virtuales, evitando cuellos de botella.
- **Formatos de salida**: Tabla resumen (`--format=summary`), JSON programático o texto filtrado por lenguaje (`--suffix`).
- **Interpretación**: Las columnas clave son Language, Files, Code, Comment y %; se incluyen pseudo-lenguajes para archivos vacíos, binarios o generados.
- **Limitaciones conocidas**: Markdown se clasifica como comentario (no código) y JSON puede subestimar líneas; para estos casos se sugieren alternativas como `wc -l`.

## Etiquetas
#análisis-de-código #pygount #métricas-de-repo #gestión-de-proyectos

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\github\codebase-inspection\SKILL.md`
