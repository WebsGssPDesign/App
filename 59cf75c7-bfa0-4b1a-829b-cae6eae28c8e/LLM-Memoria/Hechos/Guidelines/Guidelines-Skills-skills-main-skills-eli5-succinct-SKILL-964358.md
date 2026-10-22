---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/skills-main/skills/eli5-succinct/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una habilidad de IA para explicar conceptos técnicos de forma breve y clara en el chat, sin generar archivos. Su objetivo es responder preguntas complejas asumiendo que el usuario es inteligente pero nuevo en el tema, priorizando la precisión sobre la simplificación excesiva o el uso innecesario de analogías.

## Datos clave
- **Nombre:** eli5-succinct (activado por frases como "eli5", "TL;DR" o "explain like I'm five").
- **Restricción principal:** Nunca escribir archivos; las respuestas deben ser texto en chat limitado a 150 palabras.
- **Lógica de enrutamiento:** Si el usuario pide un documento para guardar, la habilidad correcta es `summary`, no esta.
- **Niveles de audiencia:** Los prefijos numéricos (eli5, eli15, eli18) ajustan el conocimiento previo asumido del lector, no la brevedad.
- **Registro técnico:** Para solicitudes como "no dumbing down", se mantiene la precisión técnica con lenguaje directo y oraciones cortas.
- **Formato de respuesta:** Empezar directamente con la conclusión; usar listas numeradas para secuencias o tablas para elementos paralelos.

## Etiquetas
#explicación #comunicación_técnica #guías_de_uso

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\skills-main\skills\eli5-succinct\SKILL.md`
