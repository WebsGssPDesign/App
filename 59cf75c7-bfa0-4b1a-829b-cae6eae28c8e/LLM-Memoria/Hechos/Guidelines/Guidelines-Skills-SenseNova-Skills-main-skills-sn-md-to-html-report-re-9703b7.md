---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/skills/sn-md-to-html-report/references/03-design-contract.md"
tags: [hecho]
---
# 03-design-contract.md

## Resumen
Este documento establece un "contrato de diseño" obligatorio antes de escribir código HTML para informes, asegurando que la implementación visual sea fiel a una planificación previa y evite caer en plantillas genéricas. Sirve como lista de verificación estricta para definir tokens, estructuras de página, tipografía y estrategias de degradación, garantizando consistencia y propósito específico en cada sección del reporte.

## Datos clave
- **Proyecto**: Sistema de diseño para informes HTML (SenseNova).
- **Tecnologías**: CSS variables (`:root`), sistemas de tokens compactos, grids asimétricos, sticky layouts.
- **Decisiones críticas**: Prohibido escribir HTML sin un `plan.md` aprobado; los tokens de espaciado y tipografía deben seguir escalas limitadas; las animaciones requieren soporte para `reduced-motion`.
- **Rutas/Flujo**: Definir contrato en `plan.md` -> Verificar "autocorrección de plantilla genérica" -> Mapear capítulo por capítulo (ej. 0=Hero, 1=Overview) -> Implementar HTML -> Auditar contra el DOM.
- **Comandos/Pasos**: Declarar variables CSS (`--bg`, `--font-body`), definir jerarquía visual, asegurar que los gráficos usen tokens de la página y no sistemas visuales separados.

## Etiquetas
#diseño-web #contrato-de-diseño #html-semántico #sistema-tokens #accesibilidad

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\skills\sn-md-to-html-report\references\03-design-contract.md`
