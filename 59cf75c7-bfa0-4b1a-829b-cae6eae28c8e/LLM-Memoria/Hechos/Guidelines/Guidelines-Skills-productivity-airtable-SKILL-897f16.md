---
fecha: 2026-10-21
etapa: aprendizaje
fuente: "Guidelines/Skills/productivity/airtable/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía explica cómo interactuar con la API REST de Airtable utilizando únicamente `curl` y un token de acceso personal (PAT), evitando dependencias como Python SDKs o servidores MCP. Su objetivo es permitir operaciones CRUD, filtrado y actualizaciones en bases de datos directamente desde la terminal mediante comandos estandarizados.

## Datos clave
- **Prerrequisitos:** Generar un PAT con scopes `data.records:read/write` y `schema.bases:read`, asegurando que el token tenga acceso explícito a las bases específicas.
- **Autenticación:** Uso obligatorio del encabezado `Authorization: Bearer $AIRTABLE_API_KEY`.
- **Comandos principales:** Listar bases (`/meta/bases`), consultar esquemas (`/bases/{ID}/tables`) y recuperar registros (`/bases/{ID}/{Table}`).
- **Filtrado avanzado:** Empleo de `filterByFormula` con codificación URL automática vía Python para consultas complejas.
- **Mutaciones:** Creación individual o en lotes (máximo 10 registros por petición) usando el parámetro `"typecast": true` para coerción automática de tipos.
- **Limitaciones:** Límite de tasa de 5 peticiones por segundo por base; manejo de errores `429` mediante retroceso.

## Etiquetas
#Airtable #API #Curl #Productividad #Automatización

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\productivity\airtable\SKILL.md`
