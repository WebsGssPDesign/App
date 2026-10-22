---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/wgoodall01/temporal-webpack-isolation-repro"
tema: "Temporal Workflow Isolation"
tags: [web]
---
# wgoodall01/temporal-webpack-isolation-repro

## Resumen
Este texto documenta un bug crítico en el SDK de TypeScript de Temporal donde la aislamiento del estado de los módulos por flujo de trabajo se desactiva silenciosamente. El problema ocurre cuando WebPack versión 5.108.0 o superior cambia la sintaxis de su código generado, rompiendo una sustitución de cadena exacta que el SDK utiliza para inyectar un proxy de caché. Esto provoca que los flujos de trabajo compartan incorrectamente variables a nivel de módulo y promesas entre ejecuciones distintas en el mismo hilo.

## Datos clave
- **Causa raíz**: WebPack ≥ 5.108.0 emite `const __webpack_module_cache__` en lugar de `var`, lo que hace fallar la búsqueda exacta del SDK (`String.replace`).
- **Impacto**: El estado de los módulos (variables, promesas) se filtra entre diferentes ejecuciones de flujos de trabajo dentro de un mismo worker.
- **Síntomas**: Flujos de trabajo colgados silenciosamente esperando promesas dejadas por otros flujos; degradación del rastreo OpenTelemetry; historiales de ejecución no rejugables (no determinismo).
- **Versión afectada**: `@temporalio/worker` 1.19.0 con WebPack ≥ 5.108.0 (dentro del rango dependiente `^5.106.2`).
- **Solución temporal**: Forzar a WebPack que emita código usando `var` en lugar de `const`.

## Etiquetas
#temporal #webpack #bug #isolación #typescript #devops

Fuente: https://github.com/wgoodall01/temporal-webpack-isolation-repro
