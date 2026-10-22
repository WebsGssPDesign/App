---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/venv_proyecto/Lib/site-packages/fastapi/.agents/skills/fastapi/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento establece las mejores prácticas y convenciones para desarrollar APIs con FastAPI, enfocándose en mantener el código limpio, seguro y optimizado. Sirve como guía técnica para escribir nuevas funcionalidades o refactorizar código existente, asegurando la compatibilidad con las últimas versiones de la librería.

## Datos clave
- **Comandos CLI**: `fastapi dev` (desarrollo con recarga) y `fastapi run` (producción).
- **Configuración**: Definir el punto de entrada en `pyproject.toml` bajo `[tool.fastapi]`.
- **Sintaxis preferida**: Usar siempre `Annotated` para parámetros (`Path`, `Query`) y dependencias (`Depends`).
- **Prohibido**: No usar elipsis (`...`) como valores por defecto en Pydantic ni en operaciones de ruta.
- **Rendimiento**: Evitar respuestas JSON obsoletas; declarar tipos de retorno explícitos para validación y serialización en Rust.
- **Routers**: Preferir configurar prefijos y etiquetas directamente en el objeto `APIRouter` antes de incluirlo.

## Etiquetas
#FastAPI #Python #Backend #BestPractices

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\venv_proyecto\Lib\site-packages\fastapi\.agents\skills\fastapi\SKILL.md`
