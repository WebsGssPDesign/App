---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/guia-configuracion-marketplace-n8n.md"
tags: [hecho]
---
# guia-configuracion-marketplace-n8n.md

## Resumen
Esta guía detalla cómo configurar un flujo automatizado en n8n que captura consultas de Facebook Marketplace hacia una base de datos PostgreSQL, permitiendo analizar el interés por productos específicos. El sistema requiere conectar la API de Messenger con un webhook público (vía ngrok) y extraer metadatos del mensaje para registrar quién preguntó, qué producto consultó y cuándo ocurrió la interacción.

## Datos clave
- **Infraestructura**: Docker con servicios `postgres:16` y `n8nio/n8n`.
- **Base de datos**: Tabla `marketplace_inquiries` con índices en `product_name` y `asked_at`; credenciales internas (host `postgres`, usuario `n8n`).
- **APIs de Meta**: Uso de `pages_messaging` para webhooks y Graph API v21.0 para obtener nombres de usuarios; requiere App Review aprobado para modo Live.
- **Herramientas externas**: ngrok para exponer localmente el puerto 5678 como HTTPS público (`TU-DOMINIO.ngrok-free.app`).
- **Lógica del flujo**: Extracción de datos vía 3 vías (referral, adjuntos o manual) guardando la fuente en `product_source`; manejo de duplicados mediante `message_id` único.

## Etiquetas
#n8n #FacebookMarketplace #PostgreSQL #Automatización #MetaAPI

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\guia-configuracion-marketplace-n8n.md`
