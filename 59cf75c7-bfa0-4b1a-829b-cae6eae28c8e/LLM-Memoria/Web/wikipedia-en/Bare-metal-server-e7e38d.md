---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://en.wikipedia.org/wiki/Bare-metal_server"
tema: "Kubernetes Cluster Autoscaler"
tags: [web]
---
# Bare-metal server

## Resumen
Un servidor bare-metal es un equipo físico dedicado exclusivamente a un solo usuario, sin utilizar virtualización ni compartir hardware con otros inquilinos. Esta configuración elimina riesgos de seguridad y efectos de vecinos ruidosos asociados a los hipervisores, ofreciendo mayor rendimiento e aislamiento. Aunque tradicionalmente se alojaban en centros de datos propios, ahora existen modelos de nube (BMaaS) que gestionan este hardware como un servicio escalable para entornos de baja latencia o computación de borde.

## Datos clave
- **Aislamiento total**: Evita el "efecto vecino ruidoso" y vulnerabilidades del hipervisor como Spectre, Meltdown o Rowhammer.
- **BMaaS (Bare-Metal-as-a-Service)**: Modelos que ofrecen servidores físicos sin hipervisores pero con automatización de ciclo de vida similar a la nube.
- **Historia**: Los primeros servidores (década de 1960) eran bare-metal; el cambio a PCs comerciales en los años 80 popularizó la virtualización.
- **Componentes seleccionables**: RAM, núcleos CPU, discos locales, GPU, FPGA y SmartNICs elegidos desde un pool para ajustar necesidades específicas.
- **Uso en edge computing**: Ideal para baja latencia en aplicaciones de realidad aumentada, coches conectados y telerobotica.

## Etiquetas
#servidores #bare-metal #BMaaS #seguridad #cloud-computing

Fuente: https://en.wikipedia.org/wiki/Bare-metal_server
