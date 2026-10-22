---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-image-doctor/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía documenta la habilidad de diagnóstico `sn-image-doctor` para el proyecto SenseNova-Skills, diseñada para validar la instalación del entorno, verificar dependencias de Python y configurar variables de entorno faltantes antes de ejecutar otras tareas. Su función principal es asegurar que la infraestructura esté operativa mediante comprobaciones automáticas e interactivas, sugiriendo reinicios si los cambios no se aplican correctamente.

## Datos clave
- **Proyecto**: SenseNova-Skills (capa 0).
- **Ruta de ejecución**: `python scripts/check_environment.py` o `python skills/sn-image-doctor/scripts/check_environment.py`.
- **Comandos importantes**: `--verbose` para diagnóstico detallado, `pip install -r skills/sn-image-base/requirements.txt` para instalar dependencias.
- **Variables críticas**: `SN_API_KEY`, `SN_BASE_URL`, `SN_IMAGE_GEN_API_KEY` (se guardan en `.env`).
- **Pasos de solución**: Verificar existencia del directorio `sn-image-base` y usar `curl` para probar conectividad de API.

## Etiquetas
#diagnóstico #SenseNova-Skills #infraestructura

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-image-doctor\SKILL.md`
