---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/software-development/requesting-code-review/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define un flujo de trabajo automatizado para la verificación de código antes del commit, diseñado para prevenir errores de seguridad y regresiones. Su función principal es orquestar una serie de pasos que incluyen escaneos estáticos, pruebas basales, revisiones por parte de agentes independientes y bucles de corrección automática.

## Datos clave
- **Proyecto:** Skill `requesting-code-review` (versión 2.0.0) para desarrollo impulsado por subagentes.
- **Tecnologías:** Git, Python, Node.js, Rust, Go; herramientas como pytest, ruff, cargo clippy y eslint.
- **Decisiones clave:** Principio de "no auto-verificación" (un agente no verifica su propio trabajo); regla "fail-closed" para el revisor independiente.
- **Pasos importantes:**
  1. Obtener el diff (`git diff --cached`).
  2. Escaneo estático de seguridad (detección de secretos, inyecciones SQL/Shell).
  3. Ejecución de pruebas y linting comparando fallos basales vs nuevos.
  4. Checklist manual rápido.
  5. Delegación a un subagente revisor independiente vía `delegate_task`.
  6. Evaluación combinada de resultados.
  7. Bucle de auto-corrección (máximo 2 ciclos) con un tercer agente.

## Etiquetas
#seguridad #calidad-de-código #automatización #git #desarrollo-agil

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\software-development\requesting-code-review\SKILL.md`
