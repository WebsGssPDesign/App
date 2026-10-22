---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/rookLab/react-component-caching"
tema: "React Server Components Caching"
tags: [web]
---
# rookLab/react-component-caching

## Resumen
React Component Caching es una biblioteca para acelerar el renderizado del lado del servidor en React 16 mediante la caché de componentes. Permite utilizar estrategias simples o plantillas y soporta implementaciones de caché como LRU, Redis o Memcached. Todas las funciones de renderizado son asíncronas y devuelven promesas que deben resolverse antes de mostrar el contenido.

## Datos clave
- **Métodos de renderizado**: `renderToString`, `renderToStaticMarkup`, `renderToNodeStream`, `renderToStaticNodeStream`.
- **Instanciación**: Se crea una instancia (`new ReactCC.ComponentCache()`) y se pasa como segundo argumento a los métodos de renderizado.
- **Marcado**: Para caché básico, añadir la propiedad `cache` al componente; para plantillas, añadir también `templatized` con un array de props.
- **Implementaciones de caché**: LRU (por defecto), Redis y Memcached.
- **Streaming**: Mejora el tiempo hasta el primer byte, pero actualmente no es compatible con la estrategia de plantillas.
- **Memcached**: Requiere pasar `memLife` (tiempo de vida en segundos) como tercer argumento opcional.

## Etiquetas
#React #ServerSideRendering #Caching #NodeJS #Performance

Fuente: https://github.com/rookLab/react-component-caching
