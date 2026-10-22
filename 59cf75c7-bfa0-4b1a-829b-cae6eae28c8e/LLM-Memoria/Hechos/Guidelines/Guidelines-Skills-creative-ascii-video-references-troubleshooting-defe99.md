---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/troubleshooting.md"
tags: [hecho]
---
# troubleshooting.md

## Resumen
Este documento actúa como guía de solución de problemas para el desarrollo de videos ASCII, detallando errores comunes en renderizado, manipulación de arrays con NumPy y limitaciones del procesamiento paralelo. Su objetivo es ayudar a los desarrolladores a diagnosticar fallos visuales (como salidas negras o texto ilegible) y evitar bloqueos técnicos al implementar efectos complejos.

## Datos clave
- **Errores de renderizado:** Ajustar gamma del tonemap, usar `screen` en lugar de `overlay` para capas oscuras, y evitar modos como `multiply` o `colordodge` sin manejo de división por cero.
- **NumPy Broadcasting:** Siempre aplicar `.copy()` después de `broadcast_to()` para evitar arrays read-only; preferir `+` sobre `+=` al mezclar formas de array distintas.
- **Multiprocesamiento:** Definir todas las funciones de escena (`fx_*`) a nivel de módulo (evitar lambdas o closures) para permitir el *pickling*; usar `np.random.RandomState` explícito para ruido determinista en macOS y Linux.
- **Comandos/Funciones críticas:** `apply_text_backdrop()`, `reverse_vignette`, `hsv2rgb`, detección de hardware (`detect_hardware`).

## Etiquetas
#ascii-video #debugging #numpy #multiprocessing #rendering

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\troubleshooting.md`
