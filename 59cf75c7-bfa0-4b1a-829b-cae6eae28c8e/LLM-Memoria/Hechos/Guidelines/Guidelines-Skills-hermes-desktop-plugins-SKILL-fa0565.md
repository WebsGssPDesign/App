---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/hermes-desktop-plugins/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe cómo crear plugins para la aplicación de escritorio Hermes que añaden elementos de interfaz como paneles y comandos sin necesidad de compilación. Sirve como guía técnica para desarrollar extensiones en JavaScript ESM que se cargan dinámicamente, permitiendo a los usuarios personalizar la UI y acceder a datos del gateway RPC.

## Datos clave
- **Proyecto**: Hermes Desktop Plugins (versión 1.0.0).
- **Tecnologías**: JavaScript ESM, React (sin compilación), `@hermes/plugin-sdk`.
- **Ruta de instalación**: `$HERMES_HOME/desktop-plugins/<id>/plugin.js` dentro del directorio de plugins activos.
- **Pasos importantes**:
  - Crear el archivo desde la plantilla relativa al directorio del skill.
  - Usar `host.request()` para llamadas JSON-RPC y `host.onEvent()` para suscripciones en tiempo real.
  - Registrar UI mediante `ctx.register` con áreas como `'panes'`, `'statusBar'` o rutas completas.
- **Restricciones críticas**: No hardcodear colores (usar variables de tema), evitar polling rápido y asegurar que los componentes importados existan realmente.

## Etiquetas
#hermes #plugins #javascript #ui-development

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\hermes-desktop-plugins\SKILL.md`
