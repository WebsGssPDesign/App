---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/conversations/Dola_estrategia/scrap/readme.md"
tags: [hecho]
---
# readme.md

## Resumen
Este archivo documenta las reglas de procesamiento y los comandos disponibles para scripts que actualizan datos de productos, como costos y márgenes. Su función principal es guiar el uso seguro de estas herramientas mediante la eliminación de campos redundantes, la creación automática de respaldos y el manejo de errores en datos inválidos.

## Datos clave
- **Reglas de formato**: Los valores monetarios deben guardarse siempre como cadenas (strings) con dos decimales.
- **Optimizaciones**: El campo `costoTotal` se elimina automáticamente por ser redundante, salvo que se comente la línea de borrado.
- **Seguridad**: Se genera un archivo `_backup.json` antes de cualquier modificación en el original.
- **Comandos principales**:
  - `node update-margin.js <porcentaje>`: Cambia el margen de ganancia.
  - `node update-costs.js <tasa> <margen>`: Recalcula costos con tasa e IVA específicos.
  - `node update-rate.js <tasa>`: Actualiza solo la tasa manteniendo márgenes actuales.
  - `node generate-platform-descriptions.js <plataforma>`: Genera descripciones para Meta, MercadoLibre o Web.

## Etiquetas
#procesamiento #scripts #backup #datos

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\conversations\Dola_estrategia\scrap\readme.md`
