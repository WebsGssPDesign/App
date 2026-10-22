---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-infographic/references/prompts-critic-system.md"
tags: [hecho]
---
# prompts-critic-system.md

## Resumen
Este documento define un rol de juez experto para evaluar la calidad visual de diagramas generados por modelos. Sirve como guía estricta para detectar errores en estructura, diseño, texto y conectores, devolviendo un informe JSON con el estado (PASS/FAIL) y sugerencias de corrección específicas.

## Datos clave
- **Proyecto**: SenseNova-Skills (evaluación de infografías).
- **Tecnologías**: Evaluación visual, generación de imágenes, formato JSON estricto.
- **Decisiones**: Se establecen 9 reglas de veto ("Red Lines") que causan un fallo inmediato; se excluye el redimensionamiento del canvas en las sugerencias.
- **Pasos importantes**: El sistema debe analizar la imagen contra categorías como completitud estructural, distribución espacial y legibilidad textual, extrayendo detalles específicos (como porcentajes de posición) para cada violación detectada.

## Etiquetas
#evaluacion_visual #diagramas #sensenova #guias_de_rol

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-infographic\references\prompts-critic-system.md`
