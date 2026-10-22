---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/note-taking/obsidian/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define las mejores prácticas para gestionar archivos en una bóveda de Obsidian priorizando herramientas nativas sobre comandos de línea. Su objetivo es asegurar la integridad de los datos y manejar correctamente rutas con espacios mediante flujos de trabajo estructurados como lectura, búsqueda, creación y edición.

## Datos clave
- **Ruta de la bóveda**: Usar la variable `OBSIDIAN_VAULT_PATH` o el fallback `~/Documents/Obsidian Vault`. Resolver rutas absolutas antes de usar herramientas de archivo para evitar problemas con espacios.
- **Herramientas preferidas**: `read_file`, `search_files`, `write_file` y `patch` en lugar de comandos como `cat`, `grep`, `find` o `ls`.
- **Búsqueda**: Usar `target: "files"` para listar notas (`pattern: "*.md"`) y `target: "content"` con `file_glob: "*.md"` para buscar texto.
- **Edición**: Crear notas completas con `write_file`; usar `patch` para anexos anclados a encabezados estables; usar `terminal` solo si es la opción más clara y segura para anexos simples sin contexto estable.
- **Enlaces**: Utilizar sintaxis de wikivínculos `[[Nombre de Nota]]` al crear contenido nuevo.

## Etiquetas
#obsidian #gestión_de_conocimiento #automatización #guía_técnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\note-taking\obsidian\SKILL.md`
