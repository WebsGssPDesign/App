---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/manim-video/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Este documento actúa como guía de solución de problemas para el desarrollo de videos con Manim, abordando errores comunes en LaTeX, agrupación de objetos y animaciones. Su objetivo es ayudar a los creadores a depurar rápidamente fallos técnicos y optimizar el rendimiento durante la producción.

## Datos clave
- **Errores de LaTeX**: Uso incorrecto de cuerdas crudas (`r""`), llaves desbalanceadas o falta del paquete `mathrsfs`.
- **Gestión de grupos**: Diferencia crítica entre `VGroup` (solo formas) y `Group` (mezcla con texto); `FadeOut` debe usar `Group(*self.mobjects)`.
- **Limitaciones de Group**: Métodos `save_state()` y `restore()` no están implementados; se recomienda animar objetos individuales o usar transformaciones visuales.
- **Texto y espaciado**: El parámetro `letter_spacing` es inválido en `Text`; se debe usar `MarkupText` con atributos Pango.
- **Animaciones**: Errores por falta de creación previa del objeto, uso incorrecto de `ReplacementTransform`, animaciones duplicadas o conflictos con actualizadores (`suspend_updating`).
- **Rendimiento y renderizado**: Uso de `-ql` para pruebas rápidas, ajuste de resolución superficial y limpieza de caché en `media/`.

## Etiquetas
#Manim #Troubleshooting #PythonAnimation #LaTeX

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\manim-video\references\troubleshooting.md`
