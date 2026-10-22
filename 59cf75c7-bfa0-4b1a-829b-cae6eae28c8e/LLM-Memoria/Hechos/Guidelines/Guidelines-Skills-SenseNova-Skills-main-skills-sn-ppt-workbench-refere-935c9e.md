---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-ppt-workbench/references/gateway-auth.md"
tags: [hecho]
---
# gateway-auth.md

## Resumen
Este documento detalla la configuración de autenticación entre el servidor Node.js del Workbench y la API del Hermes Gateway para habilitar un puente de sesión bidireccional. Su objetivo es garantizar que ambas componentes utilicen claves de acceso coincidentes (`API_SERVER_KEY` y `WORKBENCH_GATEWAY_API_KEY`) para validar las solicitudes, evitando errores de autenticación como HTTP 401 y asegurando la conectividad correcta en modo "writable".

## Datos clave
- **Proyecto**: Hermes Gateway API Auth Setup for PPT Workbench.
- **Tecnologías**: Node.js (Workbench), Python (scripts), Hermes Gateway, curl para pruebas.
- **Variables críticas**: `API_SERVER_KEY` (Gateway), `WORKBENCH_GATEWAY_API_KEY` (Workbench), `AI_GATEWAY_API_KEY` (fallback).
- **Puerto por defecto**: 8642 (bind a 127.0.0.1).
- **Ruta de configuración**: `~/.hermes/.env`.
- **Comandos importantes**:
    - Inicialización: `export WORKBENCH_GATEWAY_API_KEY=ppt-editor-dev` y `HERMES_GATEWAY_BASE_URL="http://127.0.0.1:8642"`.
    - Lanzamiento: `python $SKILL_DIR/scripts/open_workbench.py --deck-dir "$DECK"`.
    - Verificación de estado: `curl http://127.0.0.1:8642/v1/models -H "Authorization: Bearer ppt-editor-dev"`.
- **Pasos de solución**: Si falla la conexión, verificar que las claves coincidan y reiniciar el proceso del Workbench (`taskkill`) para evitar sesiones antiguas en modo "mirror-only".

## Etiquetas
#autenticación #hermes-gateway #workbench #python #nodejs

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-ppt-workbench\references\gateway-auth.md`
