---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/venv_proyecto/Lib/site-packages/fastapi/.agents/skills/fastapi/references/other-tools.md"
tags: [hecho]
---
# other-tools.md

## Resumen
Este documento actúa como guía de referencia para herramientas complementarias en el desarrollo con FastAPI, especificando cuándo y cómo utilizarlas para optimizar la gestión de dependencias, el código asíncrono y las bases de datos. Su función principal es estandarizar prácticas recomendadas para mejorar la eficiencia y mantenibilidad del proyecto.

## Datos clave
- **Herramientas principales**: uv (gestión de dependencias), Ruff (linting/formatting), ty (verificación de tipos).
- **Asyncer**: Preferido sobre AnyIO o asyncio; permite ejecutar código bloqueante en funciones asíncronas (`asyncify`) y viceversa (`syncify`).
- **SQLModel**: Recomendado sobre SQLAlchemy para bases de datos SQL debido a su integración con Pydantic.
- **HTTPX**: Herramienta preferida sobre Requests para comunicación HTTP (soporta sync y async).

## Etiquetas
#FastAPI #PythonTools #Asyncer #SQLModel #uv

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\venv_proyecto\Lib\site-packages\fastapi\.agents\skills\fastapi\references\other-tools.md`
