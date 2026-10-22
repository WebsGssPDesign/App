---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/cerebroTeam/Sistema_ERP_CRM_IA_GSSP/IA/GUIA_MEJORAS.md"
tags: [hecho]
---
# GUIA_MEJORAS.md

## Resumen
Esta guía documenta la actualización a las versiones 3.0 y 4.0 de los scripts de búsqueda web e IA, integrándolos en un nuevo sistema orquestador para automatizar investigaciones completas. El objetivo es mejorar significativamente el rendimiento mediante caché local, robustez ante fallos con lógica de reintentos y una arquitectura más limpia para la gestión del contexto y el logging.

## Datos clave
- **Archivos actualizados**: `busqueda_web_v4.py` (caché SQLite, extracción limpia de HTML), `ia_module_v3.py` (Singleton, logging real, prompts modulares) y nuevo `sistema_investigacion.py`.
- **Pipeline 1**: `investigar_tema` para búsqueda + análisis + resumen en KB.
- **Pipeline 2**: `monitorear_competencia` para análisis estratégico de precios.
- **Pipeline 3**: `generar_contenido_marketing` para redes sociales y emails.
- **Pipeline 4**: `analizar_oportunidad` para evaluar viabilidad de negocios.
- **Comandos de implementación**: Backup de archivos antiguos (`mv ..._OLD.py`) y copia de los nuevos scripts (`cp busqueda_web_v4.py busqueda_web.py`).
- **Dependencias requeridas**: `ddgs`, `openai`, `beautifulsoup4`, `requests`.

## Etiquetas
#IA #Automatización #Python #ERP #GSSP

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\cerebroTeam\Sistema_ERP_CRM_IA_GSSP\IA\GUIA_MEJORAS.md`
