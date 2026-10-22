---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Guidelines/Skills/apple/apple-reminders/SKILL.md"
tags: [hecho]
---
# SKILL.md

## Resumen
Este documento describe el uso de la herramienta `remindctl` para gestionar la aplicación Apple Reminders desde la terminal en macOS, permitiendo crear, listar y completar tareas que se sincronizan con dispositivos iOS. Sirve como guía operativa para diferenciar entre recordatorios del sistema y alertas de agentes, asegurando que las tareas aparezcan correctamente en el ecosistema de Apple.

## Datos clave
- **Proyecto**: apple-reminders (versión 1.0.0).
- **Tecnologías**: macOS, iCloud, EventKit (vía `remindctl`).
- **Instalación**: `brew install steipete/tap/remindctl`.
- **Comandos principales**:
    - Verificar estado: `remindctl status`, `remindctl authorize`.
    - Crear recordatorio: `remindctl add --title "Título" --due "Fecha" --alarm "Hora alerta"`.
    - Gestionar listas: `remindctl list [Nombre] --create` o `--delete`.
    - Completar/Borrar: `remindctl complete ID`, `remindctl delete ID --force`.
- **Diferencia crítica**: El flag `--due` establece la fecha de vencimiento, mientras que `--alarm` configura el disparador de notificación (EventKit). Se recomienda usar `--json` para scripts.

## Etiquetas
#apple-reminders #macos #automation #task-management

Fuente: `F:\automatizaciones\homeLab\Guidelines\Skills\apple\apple-reminders\SKILL.md`
