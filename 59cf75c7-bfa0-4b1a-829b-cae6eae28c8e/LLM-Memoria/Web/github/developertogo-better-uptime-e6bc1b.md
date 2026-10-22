---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/developertogo/better-uptime"
tema: "OpenTelemetry Synthetic Monitoring"
tags: [web]
---
# developertogo/better-uptime

## Resumen
BetterUptime es una plataforma de observabilidad y monitoreo alojada en el propio servidor que utiliza Rails 8 nativo sin contenedores Docker. Integra trazado distribuido mediante OpenTelemetry, pruebas sintéticas multi-protocolo y gestión de incidentes en tiempo real con una interfaz optimizada para velocidad.

## Datos clave
- **Tecnología:** Ruby 3.3+, Rails 8.0, Tailwind CSS, Hotwire (Turbo Drive).
- **Almacenamiento:** Arquitectura intercambiable soportando SQLite (WAL), Redis y ClickHouse.
- **Protocolos de prueba:** HTTP/S, SSL, ICMP Ping, TCP Port y DNS.
- **Comandos principales:** `./bin/setup_project.sh` (instalación), `bin/dev` (servidor web), `bundle exec rails runner "ProbeRunnerJob.perform_now"` (ejecución de pruebas).
- **Seguridad:** OWASP Top 10, Rata limiting, BCrypt, TOTP 2FA y SSO (SAML/OIDC).
- **Rendimiento:** Latencia sub-milisegundo, búsqueda global <10ms (`⌘K`).

## Etiquetas
#monitoreo #observabilidad #ruby-on-rails #open-telemetry #devops

Fuente: https://github.com/developertogo/better-uptime
