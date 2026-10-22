---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/briefing.schema.md"
tags: [hecho]
---
# briefing.schema.md

## Resumen
Este documento define el contrato de datos para `briefing.json`, un mapa preliminar generado por la IA en modo 'heavy' antes del análisis profundo. Establece una estructura JSON estricta con 12 campos obligatorios para capturar objetivos, entidades, terminología y vacíos de conocimiento sin permitir extensiones no autorizadas.

## Datos clave
- **Estructura**: 12 campos raíz requeridos (`user_confirmations_needed`, `task_interpretation`, `context_entities`, etc.).
- **Validación**: Prohibido añadir campos fuera de la lista; IDs globales únicos para preguntas y opciones.
- **Campos críticos**:
    - `user_confirmations_needed`: Bloqueantes (máx 3), alto valor u opcionales con opciones 2–4 y lógica de defecto.
    - `context_entities`: Mínimo 5 entradas no repetidas (tipo: empresa, tecnología, persona).
    - `knowledge_topology`: Consensos (mín 2), disputas (mín 1) y vacíos informativos.
    - `information_landscape`: Categorías de fuentes, URLs de alto valor (sin credenciales) y barreras de acceso.
- **Tipos enumerados**: `uncertainty_type` (ej. goal, scope), `research_type_inferred` (ej. academic, legal), `time_focus`.

## Etiquetas
#SenseNova #DeepResearch #SchemaDesign #DataContract

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\briefing.schema.md`
