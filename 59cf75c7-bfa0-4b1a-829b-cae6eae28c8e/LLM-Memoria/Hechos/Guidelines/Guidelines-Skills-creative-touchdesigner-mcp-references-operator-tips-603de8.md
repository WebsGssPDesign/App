---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/operator-tips.md"
tags: [hecho]
---
# operator-tips.md

## Resumen
Este documento ofrece patrones reutilizables para configurar escenas en TouchDesigner mediante Python, enfocándose específicamente en el renderizado de geometría tipo wireframe y la implementación de bucles de retroalimentación (feedback) para simulaciones. Sirve como guía técnica para evitar errores comunes al conectar nodos y asegura que las configuraciones de materiales, cámaras y resoluciones sean consistentes.

## Datos clave
- **Patrón Wireframe**: Uso de `wireframeMAT` con sufijo en mayúsculas; la geometría SOP debe crearse dentro del comp geometryCOMP y asignar el material vía `geo.par.material`.
- **Configuración Render**: Definir resolución personalizada (`custom`) y conectar explícitamente cámara y geometría usando rutas de string (`geo.path`).
- **Feedback TOP**: Estructura donde la salida inicial se conecta a la entrada del feedback, que luego alimenta al procesamiento; requiere `par.resetpulse.pulse()` para reiniciar el estado.
- **Errores comunes**: Falta de fuentes ("Not enough sources") si no se conecta un estado inicial (ej. Constant TOP negro) o resoluciones desiguales entre nodos.
- **Optimización GLSL**: Uso de formato `rgba32float` y funciones `smoothstep` para suavizar bordes en simulaciones celulares o de ondas.

## Etiquetas
#TouchDesigner #PythonAPI #Wireframe #FeedbackLoop #Simulación

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\operator-tips.md`
