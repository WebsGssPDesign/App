---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/.md/paso-a-paso-desde-cero.md"
tags: [hecho]
---
# paso-a-paso-desde-cero.md

## Resumen
Este documento establece un protocolo de trabajo híbrido para desarrollar un juego de estrategia espacial en Godot, donde el desarrollador crea manualmente la estructura base y los datos críticos para evitar errores de IA. Su objetivo es guiar paso a paso la configuración del proyecto, la creación de archivos JSON iniciales y el desarrollo de un backend mínimo en Node.js antes de implementar la lógica visual.

## Datos clave
- **Proyecto**: Godot 4.x con renderer "Compatibility" para exportación Web/HTML5.
- **Estructura manual**: Carpetas `escenas`, `scripts`, `recursos_datos` y `assets`.
- **Datos iniciales**: Archivos JSON (`edificios.json`, `tecnologias.json`) definidos manualmente con costos y niveles.
- **Backend**: Servidor Express en Node.js usando SQLite para persistencia de jugador y cola de construcción (puerto 3000).
- **Comandos críticos**: `git init` al crear el proyecto; instalación de dependencias (`npm install express sqlite3 cors`).
- **Flujo de trabajo**: Validar endpoints del backend con `curl` antes de conectar la API en Godot.

## Etiquetas
#godot #backend-nodejs #estrategia-espacial #desarrollo-juegos

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\.md\paso-a-paso-desde-cero.md`
