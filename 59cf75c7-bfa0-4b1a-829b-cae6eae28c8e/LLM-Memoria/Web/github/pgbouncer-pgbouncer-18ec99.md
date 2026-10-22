---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/pgbouncer/pgbouncer"
tema: "PostgreSQL Connection Pooling"
tags: [web]
---
# pgbouncer/pgbouncer

## Resumen
pgbouncer es un gestor ligero de conexiones para PostgreSQL que permite optimizar el uso de recursos mediante la creación de pools. El proyecto ofrece instrucciones detalladas para su compilación utilizando los sistemas Autoconf o Meson, dependiendo de las preferencias del entorno y la estabilidad requerida. Además, soporta autenticación avanzada a través de PAM y LDAP, e integra funcionalidades con systemd para una gestión de servicios eficiente.

## Datos clave
- **Requisitos principales:** Libevent 2.0+, OpenSSL 1.0.1+ (para TLS), compilador C11.
- **Sistemas de construcción:** Autoconf (recomendado) y Meson (experimental).
- **Backends DNS recomendados:** c-ares (más completo) o evdns de Libevent.
- **Autenticación opcional:** Soporte para PAM, LDAP e integración con systemd.
- **Comandos de compilación Autoconf:** `./configure --prefix=/usr/local`, `make`, `make install`.
- **Comandos de compilación Meson:** `meson setup build`, `meson compile -C build`, `meson install -C build`.

## Etiquetas
#PostgreSQL #pgbouncer #Database #ConnectionPooling

Fuente: https://github.com/pgbouncer/pgbouncer
