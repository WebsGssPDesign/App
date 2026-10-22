---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/ymichael/react-thrift"
tema: "React Server Components Prerendering"
tags: [web]
---
# ymichael/react-thrift

## Resumen
Este proyecto ofrece un servicio Thrift sencillo para pre-renderizar componentes de React en el lado del servidor utilizando Node.js. Permite registrar componentes y ejecutar llamadas remotas (RPC) para obtener su HTML renderizado como texto.

## Datos clave
- **Servicio**: `react-thrift` permite la prerenderización vía RPC.
- **Método principal**: `renderComponentToString(name, props)` devuelve el HTML.
- **Excepción**: Lanza `ServerException` en caso de error.
- **Uso**: Se instancia un servidor (`new Server()`), se registran componentes (ej: "Component1") y se escucha un puerto (ej: 9090).

## Etiquetas
#react #thrift #server-side-rendering #nodejs

Fuente: https://github.com/ymichael/react-thrift
