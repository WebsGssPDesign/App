---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/SenseNova-Skills-main/docs/sn-ppt-workbench_en.md"
tags: [hecho]
---
# sn-ppt-workbench_en.md

## Resumen
Esta guía explica cómo utilizar el entorno de trabajo SN PPT Workbench para generar, inspeccionar y editar presentaciones PowerPoint mediante la interfaz web del agente SenseNova-Skills. Permite a los usuarios monitorear el progreso en tiempo real, acceder al editor para ajustes finos y solicitar análisis automáticos de calidad o modificaciones específicas a elementos seleccionados.

## Datos clave
- **Rutas principales**: `/progress` para seguimiento de generación y `/editor` para la interfaz de edición; `/` redirige según el estado.
- **Flujo de trabajo**: El agente genera un paquete de tareas (`task_pack.json`) y devuelve una URL única para iniciar la sesión sin necesidad de recargar manualmente.
- **Herramientas de selección**: Uso de "Select", "Rectangle select" y "Lasso select" para modificar títulos, formas o imágenes individuales en lugar de redactar toda la diapositiva.
- **Análisis inteligente**: Botones "Analyze deck" (consistencia narrativa) y "Analyze current page" (lectura y diseño) que devuelven hallazgos por severidad (Alta, Media, Baja).
- **Gestión de estado**: Guardado automático tras cambios drásticos; uso de "Undo/Redo" para experimentación sin perder el progreso.

## Etiquetas
#SenseNova #PPTWorkbench #GeneraciónDePresentaciones #EdiciónVisual

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\SenseNova-Skills-main\docs\sn-ppt-workbench_en.md`
