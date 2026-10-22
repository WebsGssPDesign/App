---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/raphideb/pgstat_snap"
tema: "PostgreSQL pg_stat_statements"
tags: [web]
---
# raphideb/pgstat_snap

## Resumen
La extensión PostgreSQL `pgstat_snap` permite capturar instantáneas temporales de las estadísticas acumulativas de `pg_stat_statements` y `pg_stat_activity`, solucionando la falta de información de tiempo en estos sistemas. Proporciona vistas para calcular diferencias entre ejecuciones de consultas específicas y bases de datos, facilitando el análisis del rendimiento sin reiniciar contadores constantemente.

## Datos clave
- **Requisito previo**: Cargar `pg_stat_statements` en `shared_preload_libraries`.
- **Comandos de instalación**: Copiar archivos `.sql` y `.control` al directorio de extensiones, luego ejecutar `CREATE EXTENSION pgstat_snap;`.
- **Función principal**: `CALL pgstat_snap_collect(intervalo_segundos, cantidad_ejecuciones)`.
- **Tablas creadas**: `pgstat_snap_stat_history`, `pgstat_snap_act_history`, `pgstat_snap_diff_all`, `pgstat_snap_diff`.
- **Limpieza**: Usar `SELECT pgstat_snap_reset();` o con parámetros para borrar estadísticas específicas.
- **Advertencia de rendimiento**: La recolección masiva puede generar más de 500 MB por minuto; evitar intervalos muy cortos en clusters ocupados.

## Etiquetas
#PostgreSQL #Optimización #pg_stat_statements #Monitoreo

Fuente: https://github.com/raphideb/pgstat_snap
