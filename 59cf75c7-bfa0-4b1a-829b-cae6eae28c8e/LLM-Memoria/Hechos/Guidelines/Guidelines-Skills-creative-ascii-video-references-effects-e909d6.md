---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/ascii-video/references/effects.md"
tags: [hecho]
---
# effects.md

## Resumen
Este documento define un catálogo de bloques creativos para generar patrones visuales en videos ASCII v2, diseñados para integrarse dentro de funciones de escena. Su propósito es servir como vocabulario base que los desarrolladores deben combinar y modificar para crear efectos únicos, evitando la copia literal y fomentando la personalización mediante parámetros dinámicos.

## Datos clave
- **Filosofía de diseño**: Capa múltiples efectos en lugar de uno monolítico; parametriza todo (tono, velocidad); reacciona a características de audio/video variando 2-3 parámetros; varía la configuración por sección del video.
- **Rellenos de fondo**: Implementaciones para campos sinusoidales animados (`bg_sinefield`), fuentes de video reales (`bg_video`), ruido/estático (`bg_noise`) y ruido suave tipo Perlin (`bg_smooth_noise`).
- **Sistemas de partículas**: Uso de estado persistente en el diccionario `S` para gestionar posición, velocidad y vida; emisión basada en ritmos o disparadores.
- **Conjuntos de caracteres**: Listas predefinidas para diferentes moods (energía/explosivo vs orgánico/natural) que deben seleccionarse según el proyecto.
- **Deprecación**: Las funciones antiguas v1 (`eff_rings`, `eff_vortex`, etc.) están obsoletas; se prefieren los generadores de campos de valor (`vf_*`) integrados con `_render_vf()`.

## Etiquetas
#ascii-art #generación-de-procedural #video-creativo #python

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\ascii-video\references\effects.md`
