---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/pretext/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define el uso de `@chenglou/pretext`, una librería ligera para medir y maquetar texto sin depender del DOM, ideal para demos creativas, arte generativo y juegos donde la geometría se basa en palabras. Su objetivo es permitir animaciones fluidas a 60fps y layouts complejos calculando posiciones exactas de glifos mediante canvas antes de renderizar.

## Datos clave
- **Proyecto**: `@chenglou/pretext` (versión 0.0.6 recomendada).
- **Tecnologías**: HTML5 Canvas, ESM.sh CDN, `Intl.Segmenter`, TypeScript.
- **Decisiones**: Usar fuentes proporcionales (no monoespaciadas), fondos oscuros y texto real en lugar de Lorem Ipsum.
- **Rutas/Comandos**: Importar funciones como `prepare`, `layoutWithLines` desde ESM.sh; evitar frameworks para la interacción.
- **Pasos importantes**: Sincronizar exactamente el formato de fuente (`ctx.font`) con el CSS; elegir entre medir altura (Uso 1) o renderizar manualmente cada línea (Uso 2).

## Etiquetas
#creativcoding #tipografia #canvas #pretext #generative-art

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\pretext\SKILL.md`
