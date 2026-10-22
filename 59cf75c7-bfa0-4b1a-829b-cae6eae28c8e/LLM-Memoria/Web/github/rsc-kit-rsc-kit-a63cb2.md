---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/rsc-kit/rsc-kit"
tema: "React Server Components Prerendering"
tags: [web]
---
# rsc-kit/rsc-kit

## Resumen
rsc-kit es un plugin de Vite que habilita React Server Components sin depender de un framework específico, permitiendo su despliegue en cualquier entorno compatible con Nitro. A diferencia de Next.js, mantiene el ecosistema existente y optimiza el envío de JavaScript solo cuando es estrictamente necesario por componentes del lado del cliente.

## Datos clave
- **Instalación**: `bun create rsc-kit@latest my-app` o `bunx rsc-kit@latest init`.
- **Arquitectura**: Plugin de Vite (no bundler) que genera una sola binaria compilada con `bun build --compile`.
- **Optimización**: Las rutas congeladas en tiempo de construcción no envían JavaScript ni React al navegador.
- **Backend agnóstico**: Funciona como "Backend-Answered Pages" conectando componentes server-side a backends como Laravel o Go mediante RPCs tipados.
- **Rutas tipadas**: El build genera automáticamente las rutas, deteniendo la compilación si un enlace apunta a una página inexistente.
- **Estado**: Versión 0.x (pre-1.0), con revisión de seguridad adversarial y documentación en producción.

## Etiquetas
#ReactServerComponents #VitePlugin #NitroDeployment #JavaScriptOptimization #RSC

Fuente: https://github.com/rsc-kit/rsc-kit
