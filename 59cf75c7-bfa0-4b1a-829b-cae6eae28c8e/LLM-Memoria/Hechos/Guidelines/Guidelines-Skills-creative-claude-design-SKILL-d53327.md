---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/claude-design/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define la habilidad `claude-design` para agentes en entornos CLI/API, orientando a crear artefactos HTML únicos (prototipos, landing pages) sin depender de herramientas web alojadas. Su propósito es mantener el criterio de diseño experto adaptándolo al flujo de trabajo local y combinándose con otras habilidades para casos específicos como clonación de marcas o autorización de tokens.

## Datos clave
- **Proyecto**: Skill `claude-design` (versión 1.1.0) dentro del ecosistema Hermes.
- **Tecnologías**: HTML, CSS, JavaScript (autocontenido), diseño UX/UI y prototipado.
- **Decisiones de arquitectura**: Ignorar herramientas exclusivas de la UI web alojada (`done()`, `fork_verifier_agent()`) y usar solo métodos locales disponibles en el entorno del agente.
- **Flujo de trabajo**: Priorizar el contexto (documentos de marca, repositorios existentes) antes de diseñar desde cero para evitar resultados genéricos.
- **Composición con otras skills**: Usar `popular-web-designs` para vocabulario visual de marcas conocidas y `design-md` cuando la salida sea un archivo de especificación de tokens en lugar de un artefacto renderizado.

## Etiquetas
#diseño #html #prototipado #agentes-ia #guias-técnicas

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\claude-design\SKILL.md`
