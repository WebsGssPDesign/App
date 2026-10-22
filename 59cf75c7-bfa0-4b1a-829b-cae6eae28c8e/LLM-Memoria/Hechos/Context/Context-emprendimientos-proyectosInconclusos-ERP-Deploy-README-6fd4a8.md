---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/ERP Deploy/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe un ERP modular diseñado para operar completamente offline, ideal para distribuidoras e importadoras que requieren independencia de servicios cloud. El sistema gestiona inventarios, ventas multicanal, finanzas y automatización mediante una arquitectura de cuatro capas con motor de base de datos híbrido (PostgreSQL o JSON local).

## Datos clave
- **Proyecto**: Sistema ERP Modular para gestión de importaciones y operaciones locales.
- **Tecnologías**: Express, Vite, PostgreSQL 18.4, JSONB, GIN indexes.
- **Arquitectura**: Cuatro capas (Core, Negocio, Automatización, Integración) con motor dual-mode en `/server/db.ts`.
- **Módulos clave**: Inventario con Kardex inalterable, compras con costeo logístico amortizado, CRM de fidelización y tesorería.
- **Comandos de despliegue local**: `npm install` para dependencias y `npm run dev` para iniciar el servidor en `http://localhost:3000`.
- **Funcionalidad crítica**: Bitácora de auditoría inalterable y recálculo automático de costos al marcar compras como "Recibido".

## Etiquetas
#ERP #GestiónDeInventario #DesarrolloLocal #PostgreSQL #Automatización

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\ERP Deploy\README.md`
