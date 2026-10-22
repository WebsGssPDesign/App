---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/comfyui/tests/README.md"
tags: [hecho]
---
# README.md

## Resumen
Este documento describe la suite de pruebas unitarias e integraciones en la nube para los scripts de habilidades de ComfyUI, asegurando su correcto funcionamiento lógico y conectividad con la API. Sirve como guía operativa para ejecutar las pruebas localmente o con credenciales de nube y establece las reglas para añadir nuevas pruebas al modificar el código.

## Datos clave
- **Proyecto**: Suite de pruebas para `comfyui` (hermes-agent).
- **Tecnologías**: Python, pytest, Comfy Cloud API.
- **Comandos importantes**:
  - Ejecución unitaria: `python3 -m pytest tests/ -c tests/pytest.ini -o addopts="-p no:xdist"`
  - Ejecución con nube: `COMFY_CLOUD_API_KEY="..." python3 -m pytest ...`
- **Decisiones técnicas**: Uso de `-c` y `-o` para aislar la configuración de pytest del repositorio padre (`hermes-agent`) y desactivar `pytest-xdist`.
- **Archivos clave**: `test_common.py`, `test_cloud_integration.py`, `conftest.py` (fixtures).

## Etiquetas
#ComfyUI #PruebasPython #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\comfyui\tests\README.md`
