---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/venv_proyecto/Lib/site-packages/fastapi/.agents/skills/fastapi/references/dependencies.md"
tags: [hecho]
---
# dependencies.md

## Resumen
Este documento explica las mejores prácticas para implementar la inyección de dependencias en aplicaciones FastAPI. Detalla cuándo utilizarlas, cómo manejar recursos externos con `yield` y define el alcance (`scope`) del ciclo de vida de estas dependencias. Además, recomienda evitar clases como dependencias directas a favor de funciones que instancien objetos.

## Datos clave
- **Uso recomendado**: Para lógica compleja, acceso a recursos externos, autenticación o manejo de limpieza (ej. sesiones de BD).
- **Manejo de recursos**: Usar `yield` dentro de la función de dependencia para garantizar el cierre de conexiones en el bloque `finally`.
- **Alcance (`scope`)**:
  - `"request"` (por defecto): Ejecuta la limpieza tras enviar la respuesta.
  - `"function"`: Ejecuta la limpieza tras generar los datos pero antes de enviar la respuesta al cliente.
- **Clases vs Funciones**: Crear dependencias mediante funciones que retornen instancias de clases en lugar de declarar las clases directamente como dependencias.

## Etiquetas
#FastAPI #InyecciónDependencias #Python #Backend

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\venv_proyecto\Lib\site-packages\fastapi\.agents\skills\fastapi\references\dependencies.md`
