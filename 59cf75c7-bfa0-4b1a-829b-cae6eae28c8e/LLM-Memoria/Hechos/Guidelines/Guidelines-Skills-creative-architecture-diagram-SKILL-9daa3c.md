---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/creative/architecture-diagram/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Esta guía define una habilidad para generar diagramas de arquitectura técnica profesionales y oscuros en archivos HTML autónomos con SVG incrustado. Sirve para visualizar sistemas de software, infraestructura en la nube y topologías de microservicios sin depender de herramientas externas ni claves API, permitiendo abrir el resultado directamente en cualquier navegador.

## Datos clave
- **Proyecto:** Basado en `Cocoon AI's architecture-diagram-generator`.
- **Tecnologías:** HTML5, SVG inline, CSS puro (sin JavaScript), fuente JetBrains Mono.
- **Paleta de colores:** Mapeo semántico por tipo (Frontend: cyan, Backend: esmeralda, DB: violeta, AWS: ámbar, Seguridad: rosa).
- **Pasos del flujo:** 1) Usuario describe el sistema; 2) Generar archivo HTML siguiendo el diseño; 3) Guardar con `write_file`; 4) Abrir en navegador (comandos `open` o `xdg-open`).
- **Reglas de diseño:** Uso de doble rectángulo para evitar fugas de color, flechas dibujadas antes que los componentes, y leyenda colocada fuera de todos los límites.
- **Estructura del documento:** Header con título, SVG principal, tarjetas de resumen y pie de página metadatos.

## Etiquetas
#diagramas #arquitectura #svg #infrastructure #html

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\creative\architecture-diagram\SKILL.md`
