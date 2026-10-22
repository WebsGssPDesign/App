---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/computer-use/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define el protocolo "Computer Use" para automatizar interacciones con la interfaz gráfica de escritorio en macOS, Windows y Linux sin interrumpir al usuario ni robar el foco del teclado. Su objetivo es permitir a modelos de IA ejecutar tareas como hacer clics, escribir o arrastrar elementos mientras el usuario sigue trabajando en su propia ventana.

## Datos clave
- **Flujo canónico**: Capturar la pantalla con superposiciones numeradas (SOM) -> Identificar elementos por índice (ej. `element=7`) -> Ejecutar acción (`click`, `type`, `drag`) -> Verificar estado capturando de nuevo si es necesario.
- **Tecnología subyacente**: Se basa en la librería `cua-driver` gestionada por Hermes, exponiendo una API de alto nivel para evitar el uso directo de herramientas MCP crudas.
- **Modos de captura**: `som` (imagen + índices), `vision` (solo imagen) y `ax` (árbol de accesibilidad puro).
- **Reglas críticas**: Nunca elevar ventanas (`raise_window=false`) a menos que se solicite explícitamente; mantener el enfoque en la aplicación objetivo para reducir ruido; no cambiar espacios virtuales.
- **Atajos de teclado**: Se adaptan al sistema operativo (ej. `cmd+s` en macOS vs `ctrl+s` en Windows/Linux).

## Etiquetas
#automatización #interfaz-gráfica #cross-platform #IA-agente

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\computer-use\SKILL.md`
