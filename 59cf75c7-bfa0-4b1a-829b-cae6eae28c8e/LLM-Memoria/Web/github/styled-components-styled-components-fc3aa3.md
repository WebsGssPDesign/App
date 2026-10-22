---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/styled-components/styled-components"
tema: "React Server Components"
tags: [web]
---
# styled-components/styled-components

## Resumen
Styled-components es una librería para React que permite estilizar componentes usando CSS real de manera automática y sin necesidad de nombres de clase manuales. Soporta un único API tanto para entornos del servidor (SSR) como del cliente, incluyendo React Native. El paquete ofrece tipos nativos para TypeScript y no requiere plugins de compilación adicionales.

## Datos clave
- **Instalación**: `npm install styled-components` o equivalentes en pnpm/yarn.
- **Props dinámicos**: Se prefijan con `$` (ej. `$primary`) para evitar que aparezcan en el DOM.
- **Extensión de estilos**: Crear variantes basadas en componentes ya estilizados mediante la función `styled`.
- **Polimorfismo**: Uso del prop `as` para cambiar el elemento HTML renderizado manteniendo los estilos.
- **Seudoselectores y anidamiento**: Referencia al nombre generado con `&` para usar pseudo-clases o elementos dentro de los estilos.
- **Prefijos de vendor**: Se gestionan mediante `StyleSheetManager` y la clase `prefixPlugin`, importadas desde `styled-components/plugins`.
- **Animaciones**: Definición de `@keyframes` usando la función `keyframes` con nombres escopados automáticamente.
- **Temas**: Compartición de tokens de diseño a través del contexto React, accesibles vía `props.theme`.

## Etiquetas
#React #EstilosCSS #StyledComponents #Frontend #TypeScript

Fuente: https://github.com/styled-components/styled-components
