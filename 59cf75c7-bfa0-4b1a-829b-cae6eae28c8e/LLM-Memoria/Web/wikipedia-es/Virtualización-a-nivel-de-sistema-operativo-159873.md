---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://es.wikipedia.org/wiki/Virtualizaci%C3%B3n_a_nivel_de_sistema_operativo"
tema: "Docker Compose"
tags: [web]
---
# Virtualización a nivel de sistema operativo

## Resumen
La virtualización basada en contenedores ejecuta múltiples instancias aisladas sobre un único sistema operativo del host, eliminando la sobrecarga de sistemas operativos completos. A diferencia de las máquinas virtuales tradicionales, este método requiere que todos los contenedores utilicen el mismo kernel, aunque ofrece mayor rendimiento y eficiencia.

## Datos clave
- **Conceptos**: Motor de contenedores, chroot (1982), jaulas FreeBSD, namespaces Linux (2002), cgroups (2007), LXC, Docker.
- **Ventajas**: Sin sobrecarga de SO completo, mejor rendimiento al compartir kernel, aislamiento de recursos.
- **Limitación**: Todos los huéspedes deben usar el mismo sistema operativo que el host.
- **Evolución**: De chroot a jaulas BSD, pasando por VServer/OpenVZ y culminando con Docker para gestión masiva.

## Etiquetas
#virtualización #contenedores #Docker #Linux #DevOps

Fuente: https://es.wikipedia.org/wiki/Virtualizaci%C3%B3n_a_nivel_de_sistema_operativo
