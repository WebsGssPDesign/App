---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/touchdesigner-mcp/references/particles.md"
tags: [hecho]
---
# particles.md

## Resumen
Esta guía técnica documenta la arquitectura de sistemas de partículas en TouchDesigner, diferenciando entre las modernas POPs (GPU) y el legado particleSOP (CPU). Explica cómo construir cadenas de operadores para simular física, gestionar ciclos de vida y renderizar instancias, priorizando siempre el rendimiento con POPs.

## Datos clave
- **Tecnologías**: TouchDesigner 2025.32, POP family (compute), particleSOP (legacy).
- **Decisiones**: Priorizar POPs por GPU acceleration; usar particleSOP solo para demos rápidas o <5k partículas.
- **Rutas y comandos**: `td_get_par_info` para verificar parámetros; `geometryCOMP` como contenedor principal.
- **Pasos importantes**: Crear cadena Source → Force(s) → Delete → Solver; renderizar con `glslMAT` instancing o `popCollideTOP` para colisiones.

## Etiquetas
#TouchDesigner #Particles #POP #VFX

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\touchdesigner-mcp\references\particles.md`
