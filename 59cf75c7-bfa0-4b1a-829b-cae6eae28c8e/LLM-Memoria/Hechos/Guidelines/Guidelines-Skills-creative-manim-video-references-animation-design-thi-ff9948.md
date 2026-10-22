---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/animation-design-thinking.md"
tags: [hecho]
---
# animation-design-thinking.md

## Resumen
Esta guía establece un marco de pensamiento para diseñar animaciones educativas en Manim antes de escribir código, determinando cuándo es útil mover elementos y cuándo una imagen estática es mejor. Su objetivo principal es optimizar la carga cognitiva del espectador sincronizando narración visual y auditiva mediante pausas estratégicas y beats definidos.

## Datos clave
- **Criterios de animación:** Usar movimiento para secuencias temporales, cambios espaciales o comparaciones; usar estático para diagramas simples o referencias densas.
- **Proceso de diseño:** Redactar la narración primero, identificar "beats" visuales y seleccionar herramientas específicas (ej. `Transform`, `FadeIn`) según la necesidad.
- **Reglas de ritmo:** Mínimo 2s para ecuaciones nuevas + pausa; usar `self.wait()` después de cada revelado para evitar que el espectador se quede atrás.
- **Sincronización:** El principio "ver luego oír" (aparecer visual antes del audio) y uso de `manim-voiceover` para alinear tiempos.
- **Estrategia de ecuaciones:** Mostrar la ecuación completa tenue primero, revelando términos en orden lógico de comprensión, no de escritura.

## Etiquetas
#Manim #AnimaciónEducativa #DiseñoVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\animation-design-thinking.md`
