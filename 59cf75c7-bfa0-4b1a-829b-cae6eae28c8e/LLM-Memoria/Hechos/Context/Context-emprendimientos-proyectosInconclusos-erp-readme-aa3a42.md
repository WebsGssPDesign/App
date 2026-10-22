---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/erp/readme.md"
tags: [hecho]
---
# readme.md

## Resumen
Este documento describe GSSP Mini Market ERP v2.6, un sistema de gestión empresarial diseñado para retail en Uruguay que maneja costos bimonetarios (USD/UYU) y calcula precios multicanal automáticamente. Su función principal es eliminar el cálculo manual de rentabilidad al actualizar tipos de cambio o costos de importación, integrando control de inventario y ventas en una sola plataforma.

## Datos clave
- **Proyecto**: GSSP Mini Market ERP v2.6.
- **Tecnologías**: React 19, TypeScript 5.8, Vite 6.2, Tailwind CSS v4, SQLite (sql.js).
- **Persistencia**: Archivos JSON modulares (`products.json`, `sales_mercadolibre.json`) sincronizados con localStorage y base de datos SQLite en navegador.
- **Organización de activos**: Imágenes estructuradas por SKU en `/img/<SKU>/` con fallback automático a placeholders si fallan las rutas.
- **Lógica financiera**: Cálculo automático de precios para MercadoLibre (con deducción del 15% de comisión), canales sociales y precio defensivo basado en costos en dólares convertidos a UYU.
- **Flujo de actualización**: Permite ajustar el costo de compra directamente desde la ficha del producto, disparando un recálculo inmediato de todos los precios derivados y registrando historial.

## Etiquetas
#ERP #React19 #GestiónDeInventario #Bimonetario #Uruguay

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\erp\readme.md`
