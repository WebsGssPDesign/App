---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/erp-crm-ia-local/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este proyecto es un sistema integral de ERP, CRM e Inteligencia Artificial diseñado para emprendimientos de ventas virtuales. Funciona completamente offline utilizando herramientas open source, eliminando la dependencia de APIs externas y garantizando la privacidad de los datos. Su objetivo central es automatizar la gestión de inventario, clientes y operaciones comerciales mediante análisis predictivo local.

## Datos clave
- **Tecnologías**: FastAPI (backend), React/TypeScript (frontend), PostgreSQL/SQLite, Ollama con modelo Phi-3 Mini.
- **Instalación crítica**: Requiere descargar e instalar Ollama (`ollama pull phi3:mini`) antes de ejecutar el backend.
- **Configuración**: Crear entorno virtual Python, copiar `.env.example` y editar variables como `SECRET_KEY` y credenciales de MercadoLibre.
- **Rutas principales**: Backend en `http://localhost:8000`, Frontend en `http://localhost:5173`.
- **Funcionalidad IA**: Predicción de demanda, análisis de ventas, generación de contenido y asistente de chat local.
- **Integraciones**: MercadoLibre (API oficial) e Instagram/Facebook (scraping manual vía Selenium).

## Etiquetas
#ERP #CRM #IALocal #OpenSource #FastAPI

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\erp-crm-ia-local\README.md`
