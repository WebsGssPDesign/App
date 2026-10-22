---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/dapr/go-sdk"
tema: "Dapr PubSub"
tags: [web]
---
# dapr/go-sdk

## Resumen
Este documento presenta el SDK oficial de Dapr para Go, una librería cliente diseñada para facilitar la creación de aplicaciones distribuidas aprovechando las APIs públicas del framework. El paquete incluye módulos específicos para interactuar con servicios y gestionar callbacks, priorizando una experiencia idiomática en lenguaje Go.

## Datos clave
- **Paquetes principales**: `client` (para invocar APIs públicas) y `service` (para crear servicios invocables).
- **Instalación**: Se realiza mediante el comando `go get "github.com/dapr/go-sdk/client"`.
- **Inicialización**: La función `NewClient()` crea la instancia con un timeout por defecto de 5 segundos, personalizable vía la variable de entorno `DAPR_CLIENT_TIMEOUT_SECONDS`.
- **Gestión de estado**: Métodos básicos como `SaveState`, `GetState` y `DeleteState`; operaciones avanzadas incluyen `SetStateItem`, `SaveBulkState`, `GetBulkState` y `ExecuteStateTransaction`.
- **Publicación de eventos**: Uso del método `PublishEvent` para enviar datos a un tema en componentes PubSub.
- **Invocación de servicios**: Funciones `InvokeMethod` (sin carga) y `InvokeMethodWithContent` (con carga JSON personalizada).

## Etiquetas
#Dapr #GoSDK #Microservicios #DesarrolloGo

Fuente: https://github.com/dapr/go-sdk
