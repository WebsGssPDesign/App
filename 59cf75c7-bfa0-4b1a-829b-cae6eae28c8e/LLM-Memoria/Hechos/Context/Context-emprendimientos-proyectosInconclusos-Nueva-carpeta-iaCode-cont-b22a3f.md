---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/Nueva carpeta/iaCode/.continue/rules/new-rule.md"
tags: [hecho]
---
# new-rule.md

## Resumen
Este archivo define las reglas de operación para el asistente de IA integrado en VS Code mediante la extensión Continue. Establece dos modos de trabajo: uno consultivo y otro automatizado que permite ejecutar acciones directas como crear, leer o modificar archivos y ejecutar comandos de terminal. Su objetivo es guiar al modelo para que aplique cambios de código de forma segura y eficiente sin intervención manual constante.

## Datos clave
- **Proyecto**: Configuración de reglas para la extensión Continue en VS Code.
- **Tecnologías**: VS Code, extensión Continue, sistema de archivos integrado.
- **Decisiones**: Implementación de "Agent Mode" para automatización directa y "Chat Mode" para sugerencias solo.
- **Formato de respuesta**: Uso obligatorio de placeholders `// ... existing code ...` en bloques de código para indicar modificaciones específicas.
- **Capacidades**: Crear, leer, eliminar (con confirmación), modificar archivos y ejecutar pruebas o linters vía terminal.

## Etiquetas
#vscode #continue #automatización #desarrollo #agentmode

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\Nueva carpeta\iaCode\.continue\rules\new-rule.md`
