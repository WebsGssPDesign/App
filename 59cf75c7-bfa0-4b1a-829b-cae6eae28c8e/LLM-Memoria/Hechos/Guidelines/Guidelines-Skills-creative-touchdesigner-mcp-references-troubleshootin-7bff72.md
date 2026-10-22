---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Este documento detalla procedimientos de solución de problemas para la integración del servidor MCP "twozero" en TouchDesigner. Cubre diagnósticos de conectividad, errores comunes al ejecutar herramientas de Python, gestión de parámetros y optimización de rendimiento bajo licencias no comerciales.

## Datos clave
- **Comandos de diagnóstico**: `pgrep TouchDesigner`, `curl http://localhost:40404/mcp`, `nc -z 127.0.0.1 40404`.
- **Herramientas críticas**: `td_get_par_info` (obligatorio para descubrir nombres de parámetros), `td_execute_python`, `td_list_instances`.
- **Formatos de operadores**: Usar camelCase con sufijo familiar (ej: `noiseTOP`, no `NoiseTop`).
- **Restricciones de licencia**: Resolución máxima 1280x1280; codificación H.264/H.265 requiere licencia comercial.
- **Configuración Hermes**: Archivo `$HERMES_HOME/config.yaml` con entrada `mcpServers`.

## Etiquetas
#TouchDesigner #MCP #Troubleshooting #PythonIntegration

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\troubleshooting.md`
