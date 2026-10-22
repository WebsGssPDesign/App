---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/accretional/collector"
tema: "gRPC Server Reflection"
tags: [web]
---
# accretional/collector

## Resumen
Collector es una plataforma de programación distribuida que combina un ORM para Protocol Buffers, un servidor CRUD y capacidades de descubrimiento de servicios en tiempo real. Su objetivo principal es actuar como nodo en una "malla de agentes", permitiendo a las LLMs descubrir y gestionar datos y herramientas de manera dinámica y tipada.

## Datos clave
- **Tecnologías base**: gRPC, Protocol Buffers, SQLite y reflexión extensiva.
- **Componentes principales**:
  - `CollectionService`: API genérica para CRUD y búsqueda sobre colecciones de protos.
  - `CollectionRepo`: Controlador de colecciones que gestiona copias de seguridad y operaciones de base de datos.
  - `CollectiveDispatcher`: Ruteo dinámico de llamadas RPC entre nodos en una malla distribuida.
  - `CollectorRegistry`: Registro de mensajes y servicios con validación de tipos.
- **Modelo de datos**: Las "Colecciones" son listas ordenadas de registros filtrables por etiquetas, almacenadas en SQLite y organizadas mediante un modelo jerárquico de nombres (namespaces) para multitenencia.
- **Arquitectura**: Cada instancia ejecuta un único servidor gRPC (puerto 50051) que integra todos los servicios; múltiples instancias se conectan vía Dispatcher para formar un sistema distribuido.

## Etiquetas
#gRPC #ProtocolBuffers #ORM #DistributedSystems #LLMTools

Fuente: https://github.com/accretional/collector
