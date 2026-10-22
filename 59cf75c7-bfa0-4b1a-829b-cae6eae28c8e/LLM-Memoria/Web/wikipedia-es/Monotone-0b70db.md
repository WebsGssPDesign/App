---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Monotone"
tema: "Git Hooks"
tags: [web]
---
# Monotone

## Resumen
Monotone es un sistema distribuido de control de versiones que prioriza la integridad criptográfica y la seguridad sobre el rendimiento bruto. Utiliza hashes SHA-1 para identificar revisiones, permite firmas RSA de usuarios y opera sin servidores centrales mediante su protocolo netsync. Aunque fue una inspiración clave para Git debido a sus ideas sobre la gestión de cambios, Monotone se distingue por rechazar técnicas como "cherry picking" para mantener la pureza del historial.

## Datos clave
- **Protocolo:** Netsync (puerto 4691), compatible con SSH desde v0.27.
- **Identificación:** Hashes SHA-1 en lugar de números secuenciales.
- **Base de datos:** SQLite local para cada participante.
- **Seguridad:** Firmas RSA y trazabilidad criptográfica.
- **Característica distintiva:** Rechazo a "cherry picking" (selección individual de commits).
- **Incompatibilidad:** La versión 0.26 introdujo cambios estructurales incompatibles con versiones anteriores.
- **Implementación:** C++ sobre Boost, Botan y SQLite; extensiones en Lua.

## Etiquetas
#controlDeVersiones #Monotone #Git #Distribuido #Criptografia

Fuente: https://es.wikipedia.org/wiki/Monotone
