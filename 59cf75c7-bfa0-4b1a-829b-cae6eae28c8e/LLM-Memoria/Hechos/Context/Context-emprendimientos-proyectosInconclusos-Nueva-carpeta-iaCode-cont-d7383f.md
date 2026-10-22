---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/Nueva carpeta/iaCode/.continue/prompts/new-prompt.md"
tags: [hecho]
---
# new-prompt.md

## Resumen
Este archivo define un prompt automatizado para un agente de desarrollo enfocado exclusivamente en pruebas unitarias. Su función es analizar el código existente, generar suites de tests completas respetando las convenciones del proyecto y ejecutarlos hasta lograr un estado estable sin errores.

## Datos clave
- **Proyecto**: `iaCode` (subcarpeta `prompts`).
- **Tecnologías**: Frameworks de testing nativos del entorno (`npm test`, `pytest`, `cargo test`) o sugerencias si faltan.
- **Pasos críticos**: Análisis de dependencias, creación de suite de tests con casos límite y manejo de errores, ejecución automática vía Agent Mode.
- **Comandos implícitos**: `npm test`, `pytest`, `cargo test`.
- **Lógica de fallo**: Ajustar código o tests para pasarlos; reportar bugs reales en lugar de forzar resultados.

## Etiquetas
#testing #automatización #qa #desarrollo

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\Nueva carpeta\iaCode\.continue\prompts\new-prompt.md`
