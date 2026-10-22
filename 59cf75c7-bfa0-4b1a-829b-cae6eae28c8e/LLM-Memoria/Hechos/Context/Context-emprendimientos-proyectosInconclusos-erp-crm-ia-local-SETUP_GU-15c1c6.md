---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/proyectosInconclusos/erp-crm-ia-local/SETUP_GUIDE.md"
tags: [hecho]
---
# SETUP_GUIDE.md

## Resumen
Esta guía detalla el despliegue local del sistema ERP CRM con inteligencia artificial, integrando Ollama para procesamiento offline y configurando los entornos de backend (Python/FastAPI) y frontend (Node.js). Su objetivo es permitir a los usuarios ejecutar la aplicación completa en su PC personal para gestionar inventario, clientes y asistencia inteligente sin depender de servicios en la nube.

## Datos clave
- **Proyecto:** ERP CRM IA Local (contexto: emprendimientos/proyectosInconclusos).
- **Tecnologías:** Ollama (phi3:mini), Python 3.9+, FastAPI, Node.js 18+, SQLite.
- **Rutas locales:** Backend en `http://localhost:8000`, Frontend en `http://localhost:5173`, Ollama en `http://localhost:11434`.
- **Comandos críticos:** `ollama pull phi3:mini`, `python -m venv venv`, `npm install`, `pip install -r requirements.txt`.
- **Pasos de configuración:** Copiar `.env.example` a `.env` y actualizar la clave secreta; verificar puertos activos.

## Etiquetas
#ERP #CRM #IALocal #Ollama #Despliegue

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\proyectosInconclusos\erp-crm-ia-local\SETUP_GUIDE.md`
