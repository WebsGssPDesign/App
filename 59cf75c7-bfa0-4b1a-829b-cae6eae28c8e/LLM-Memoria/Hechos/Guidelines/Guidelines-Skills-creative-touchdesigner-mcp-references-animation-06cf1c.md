---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/animation.md"
tags: [hecho]
---
# animation.md

## Resumen
Este documento actúa como guía técnica para implementar animaciones basadas en el tiempo en TouchDesigner, cubriendo desde fuentes de tiempo hasta métodos avanzados de suavizado. Su objetivo es estandarizar las mejores prácticas para crear movimientos fluidos, secuencias activadas y curvas personalizadas utilizando CHOPs y expresiones Python.

## Datos clave
- **Fuentes de tiempo**: `absTime.seconds` para movimiento continuo (shaders) vs `me.time.frame` para animaciones locales por componente.
- **CHOPs principales**: `lfoCHOP` para oscilación cíclica, `timerCHOP` para secuencias activadas una vez, y `patternCHOP` para formas de onda personalizadas.
- **Easing en expresiones**: Uso de funciones matemáticas nativas como `smoothstep`, `pow` y `sin` dentro de las cadenas de expresión para controlar la velocidad de transición.
- **Suavizado de datos**: `filterCHOP` (gaussian/lowpass) para reducir ruido y `lagCHOP` para simular tiempos de ataque y liberación asimétricos.
- **Flujo de trabajo**: Preferencia por CHOPs sobre scripts Python para lógica en tiempo real debido a su eficiencia CPU y determinismo.

## Etiquetas
#TouchDesigner #Animación #PythonAPI #MotionGraphics

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\animation.md`
