---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "https://github.com/pal-tamas/rask"
tema: "React Server Components Islands"
tags: [web]
---
# pal-tamas/rask

## Resumen
Rask es un framework full-stack en C# diseñado para permitir a desarrolladores individuales construir, ejecutar y desplegar productos completos utilizando una sola base de código. Se basa en ASP.NET Core y EF Core, ofreciendo componentes renderizados por el servidor o en WebAssembly, junto con soporte nativo para frameworks front-end como React o Vue mediante un sistema de "islands". Incluye funcionalidades integradas como autenticación, colas de trabajo y almacenamiento de archivos sin necesidad de servicios externos.

## Datos clave
- **Instalación:** `curl -sSL https://rask.sh/rask.sh | sh` (Linux/Mac) o `irm ... | iex` (Windows PowerShell). Alternativa: `dotnet tool install -g Rask.Cli`.
- **Integración de proyectos existentes:** `dotnet add package Rask.Server` y `dotnet add package Rask.Wasm`.
- **Creación de proyectos:** `rask new [Nombre]`, con opciones como `--islands react` para añadir componentes front-end.
- **Gestión de base de datos (SQLite por defecto):** `rask db add [NombreMigración]`.
- **Despliegue:** `rask deploy --host usuario@servidor --dominio ejemplo.com` (usa Docker y HTTPS automático).
- **Comandos principales:** `rask dev`, `rask new`, `rask db`, `rask deploy`.
- **Características incluidas:** Autenticación, jobs de fondo, correo electrónico, caché y almacenamiento de archivos en SQLite.

## Etiquetas
#Rask #CSharp #FullStack #WebAssembly #ASPNETCore

Fuente: https://github.com/pal-tamas/rask
