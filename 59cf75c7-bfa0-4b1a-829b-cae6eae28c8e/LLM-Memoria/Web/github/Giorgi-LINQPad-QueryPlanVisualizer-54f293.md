---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/Giorgi/LINQPad.QueryPlanVisualizer"
tema: "PostgreSQL Query Planning"
tags: [web]
---
# Giorgi/LINQPad.QueryPlanVisualizer

## Resumen
LINQPad.QueryPlanVisualizer es una herramienta que permite visualizar los planes de ejecución de consultas para Entity Framework y LINQ to SQL directamente dentro del entorno de desarrollo LINQPad. El software soporta bases de datos Microsoft SQL Server y PostgreSQL, facilitando el análisis del rendimiento y la identificación de índices faltantes.

## Datos clave
- **Soporte ORM**: Entity Framework Core 5 y LINQ to SQL.
- **Instalación**: Disponible como paquete NuGet o archivo DLL en la carpeta `My Documents\LINQPad Plugins`.
- **Requisito técnico**: Versión 2.X requiere Microsoft Edge WebView2 Runtime instalado para funcionar.
- **Funcionalidades principales**: Visualización del plan de ejecución, generación y creación directa de índices faltantes, exportación a servidores externos o disco local.
- **Uso**: Se invoca mediante el método estático `QueryPlanVisualizer.DumpPlan(query)` o la extensión `DumpPlan` en objetos `IQueryable`.

## Etiquetas
#LINQPad #SQLServer #PostgreSQL #EntityFramework #OptimizaciónDeConsultas

Fuente: https://github.com/Giorgi/LINQPad.QueryPlanVisualizer
