---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/design-md/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define la especificación "DESIGN.md" de Google para describir sistemas visuales a agentes de código mediante un archivo único que combina tokens YAML y explicaciones en Markdown. Su función principal es estandarizar identidades visuales, permitiendo validación automática de accesibilidad (WCAG), comparación de versiones y exportación directa a frameworks como Tailwind o formatos DTCG.

## Datos clave
- **Proyecto:** Especificación `DESIGN.md` (Apache-2.0).
- **Tecnologías:** YAML front matter, Markdown, Node.js CLI (`@google/design.md`).
- **Comandos principales:**
  - Validar estructura y contraste: `npx @google/design.md lint DESIGN.md`
  - Comparar versiones: `npx @google/design.md diff v1.md v2.md`
  - Exportar a Tailwind: `npx @google/design.md export --format tailwind`
  - Exportar a DTCG JSON: `npx @google/design.md export --format dtcg`
- **Reglas de tokens:** Referencias como `{colors.primary}` para evitar duplicidad; propiedades de componentes limitadas (ej. `backgroundColor`, `rounded`).
- **Orden canónico:** Overview, Colors, Typography, Layout, Elevation, Shapes, Components, Do's and Don'ts.

## Etiquetas
#design-system #google-spec #accessibility #tailwind #tokens

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\design-md\SKILL.md`
