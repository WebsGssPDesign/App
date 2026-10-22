---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/updaters-and-trackers.md"
tags: [hecho]
---
# updaters-and-trackers.md

## Resumen
Este documento explica cómo usar "updaters" y "ValueTrackers" en Manim para crear animaciones continuas donde objetos dependen de otros sin necesidad de reubicarlos manualmente en cada paso. La técnica permite establecer relaciones dinámicas una vez, asegurando que etiquetas, líneas o gráficos sigan a elementos móviles en tiempo real durante la reproducción del video.

## Datos clave
- **ValueTracker**: Objeto invisible que almacena un valor flotante; animarlo actualiza automáticamente todos los objetos conectados.
- **Patrón de uso**: Crear tracker -> Definir objetos dependientes con `always_redraw` o `add_updater` -> Animar el tracker.
- **Tipos de updaters**: 
  - Lambda (`add_updater`): Para cambios de posición, color u opacidad (eficiente).
  - Basado en tiempo (`dt`): Para rotación continua, simulaciones físicas y movimiento oscilatorio.
  - `always_redraw`: Reconstruye el objeto desde cero cada frame; usar solo si la estructura cambia.
- **Herramientas auxiliares**: `DecimalNumber` y `Variable` para mostrar valores numéricos en tiempo real; `turn_animation_into_updater` para convertir animaciones únicas en loops infinitos.
- **Control**: Métodos como `clear_updaters`, `suspend_updating` y `resume_updating` gestionan la interacción entre animaciones manuales y updaters automáticos.

## Etiquetas
#manim #animación #programación #visualización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\updaters-and-trackers.md`
