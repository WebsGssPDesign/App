---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-motion-html/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento define el flujo de trabajo para crear historias HTML con movimiento continuo impulsado por IA, diseñadas para narrativas inmersivas y no para páginas web genéricas. Establece un proceso estricto que prioriza la investigación, los planes visuales aprobados explícitamente por el usuario y la generación escalonada de medios antes de ejecutar cualquier comando de pago.

## Datos clave
- **Proyecto:** `sn-motion-html` (plantilla reutilizable configurable).
- **Comandos iniciales:** `python scripts/init_project.py <ruta> --title "Título" --style [anime|cinematic|cgi] --ui [folio|caption|graphic]`.
- **Flujo de aprobación:** Requiere validación explícita en dos puertas: 1) Estilo visual (incluyendo referencias de imágenes) y 2) Contenido y plan de tomas.
- **Herramientas principales:** `seedance_pipeline.py` para generar clips y conectores, `verify_media.py` para inspección y `serve_project.py` para pruebas en navegador.
- **Restricciones técnicas:** Detectar capacidad de generación de imágenes antes de crear stills; evitar inferir aprobación tácita del usuario.

## Etiquetas
#sn-motion-html #generación-de-video #narrativa-inmersiva #flujos-de-trabajo

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-motion-html\SKILL.md`
