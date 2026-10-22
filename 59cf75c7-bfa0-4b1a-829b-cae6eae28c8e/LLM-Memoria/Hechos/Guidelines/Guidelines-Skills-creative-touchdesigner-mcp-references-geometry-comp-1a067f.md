---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/geometry-comp.md"
tags: [hecho]
---
# geometry-comp.md

## Resumen
Esta guía técnica explica cómo construir y configurar Geometry COMPs en TouchDesigner para generar geometría dinámica. Su objetivo principal es asegurar que los objetos renderizados sean POPs (no SOPs) dentro del componente y detalla las mejores prácticas para instanciar formas, conectar nodos correctamente y preparar la salida de renderizado.

## Datos clave
- **Creación**: Usar `root.create(geometryCOMP)` y destruir hijos por defecto antes de añadir nuevas formas.
- **Regla de oro**: Solo los POPs (ej. `boxPOP`, `spherePOP`) se renderizan dentro del Geometry COMP; los SOPs son invisibles.
- **Instanciación**: Activar con `geo.par.instancing = True` y asignar atributos específicos según el origen (CHOP, TOP o DAT).
- **Renderizado**: Configurar `renderTOP` conectando explícitamente la cámara (`cam.path`) y la geometría (`geo.path`).
- **Morphing**: Utilizar `switchPOP` para transicionar entre diferentes formas dinámicamente.
- **Errores comunes**: No crear geometría fuera del COMP ni referenciar operadores de padres usando rutas relativas ocultas.

## Etiquetas
#TouchDesigner #GeometryCOMP #Rendering #PythonAPI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\geometry-comp.md`
