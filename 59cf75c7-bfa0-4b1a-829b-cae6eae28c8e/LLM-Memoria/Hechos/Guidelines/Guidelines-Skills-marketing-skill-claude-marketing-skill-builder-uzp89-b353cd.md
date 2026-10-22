---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/marketing-skill-claude-marketing-skill-builder-uzp891/skills/visual-brief-generator/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta habilidad convierte ideas de contenido o campañas en breves visuales estructurados, listos para copiar y pegar, que incluyen listas de escenas, prompts detallados por escena, relaciones de aspecto específicas por plataforma y guías de estilo. Su función principal es facilitar la creación de activos visuales mediante IA o servir como documento técnico si no hay herramientas conectadas, verificando siempre el estado real de las conexiones disponibles en la sesión.

## Datos clave
- **Proyecto**: `visual-brief-generator` dentro del conjunto de habilidades de marketing.
- **Tecnologías y Herramientas**: Utiliza herramientas MCP (Model Context Protocol) para generación visual; verifica dinámicamente si hay conectores activos (ej. Higgsfield, Canva) en lugar de asumirlos.
- **Flujo de trabajo**:
  1. Verifica el estado de configuración en `references/brand-voice.md`.
  2. Busca documentación relevante (`README*`, `CHANGELOG*`) para entender el contexto si el usuario no lo especifica.
  3. Genera una estructura Markdown obligatoria: *Brief Overview*, *Shot List*, *Per-Scene Prompts*, *Aspect Ratio & Format per Platform*, *Style & Mood Guide*.
  4. Si hay herramienta conectada, pregunta al usuario si desea generar el activo; de lo contrario, entrega solo el texto del breve sin inventar URLs o resultados falsos.
- **Comandos y rutas**: Uso de `printenv CLAUDE_PLUGIN_ROOT` para resolver rutas absolutas y globbing (`Glob`) para buscar archivos de documentación.

## Etiquetas
#generación-de-imágenes #breve-visual #automatización-marketing #mcp-tools

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\marketing-skill-claude-marketing-skill-builder-uzp891\skills\visual-brief-generator\SKILL.md`
