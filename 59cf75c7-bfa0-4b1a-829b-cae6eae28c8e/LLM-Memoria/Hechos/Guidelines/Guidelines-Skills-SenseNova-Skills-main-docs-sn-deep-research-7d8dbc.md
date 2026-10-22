---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-deep-research.md"
tags: [hecho]
---
# sn-deep-research.md

## Resumen
Este documento describe la arquitectura unificada de investigación profunda integrada en el repositorio SenseNova, reemplazando los flujos antiguos por un controlador centralizado. Su función es orquestar agentes especializados para recopilar evidencia, validar datos y generar informes estructurados con citas automáticas. Ofrece dos puntos de entrada: una habilidad nativa del repositorio y una CLI independiente para usuarios que requieren control explícito sobre la instalación y el progreso.

## Datos clave
- **Puntos de entrada**: `sn-deep-research` (nativo) y `sn-deepresearch-cli` (standalone).
- **Flujo principal**: El controlador gestiona modos (rápido, normal, pesado), despliega agentes (`scout`, `plan`, `research`) y ejecuta validadores estrictos.
- **Agentes especializados**: Planificación de paquetes de trabajo, recolección de evidencia por dimensión y redacción de informes finales.
- **Habilidades de búsqueda**: Incluye módulos para académicos, código, finanzas, mercados chinos y redes sociales globales (Reddit, Twitter, etc.).
- **Comando de inicio**: `/skill sn-deep-research "Home robotics supply chain"`.
- **Gestión de credenciales**: Se recomienda usar variables de entorno en un archivo `.env` en la raíz del repositorio.

## Etiquetas
#SenseNova #InvestigaciónProfunda #InteligenciaArtificial #Automatización #DocumentaciónTécnica

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-deep-research.md`
