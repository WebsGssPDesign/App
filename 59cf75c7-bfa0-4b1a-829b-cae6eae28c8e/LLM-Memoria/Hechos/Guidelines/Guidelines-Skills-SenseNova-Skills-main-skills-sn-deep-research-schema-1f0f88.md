---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-deep-research/schemas/outline.schema.md"
tags: [hecho]
---
# outline.schema.md

## Resumen
Este documento define el contrato de datos para la fase de orquestación de informes en el sistema SenseNova, especificando cómo estructurar la evidencia y los argumentos. Sirve como guía técnica para generar `outline.json` que coordina múltiples unidades de contenido, asegurando coherencia lógica, asignación precisa de citas y cumplimiento de restricciones de escritura antes del renderizado final.

## Datos clave
- **Estructura principal**: El archivo define el esquema JSON para `outline.json`, incluyendo campos como `paradigm` (comparación/evaluación), `depth_level` y `global_arc`.
- **Unidades de contenido (`content_units`)**: Soporta 1–20 unidades ordenadas con tipos específicos (`matrix`, `narrative`, `timeline`, `checklist`, etc.). Cada unidad tiene un presupuesto de palabras (50-3000) y define tareas para el lector.
- **Gestión de evidencia**: Establece límites estrictos: máximo 10 referencias por elemento, 30 afirmaciones totales por unidad, y requiere que `evidence_subset` coincida exactamente con las referencias internas.
- **Ruteo de afirmaciones (`claim_routing_table`)**: Obliga a asignar una única unidad principal para cada afirmación citada, permitiendo roles secundarios solo como contexto o referencia.
- **Contrato de estilo**: Permite definir registros (ej. `executive_memo`) y voces mediante el objeto `style_contract`.
- **Rutas de archivos**: Los datos se guardan en `{report_dir}/outline.json` y subunidades evidenciales en `{report_dir}/content_units/{unit_id}.json`.

## Etiquetas
#SenseNova #OrquestaciónDeInformes #ContratoDeDatos #IAGenerativa

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-deep-research\schemas\outline.schema.md`
