---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "https://github.com/nianticlabs/venator"
tema: "Kubernetes CronJobs"
tags: [web]
---
# nianticlabs/venator

## Resumen
Venator es una plataforma de detección de amenazas flexible que gestiona reglas mediante K8s CronJob y Helm, aunque también puede ejecutarse de forma independiente o con otros programadores como Nomad. Su diseño modular permite ejecutar cada regla como un trabajo aislado para facilitar la gestión, el mantenimiento y la integración con múltiples motores de consulta y destinos de publicación.

## Datos clave
- **Gestión de reglas**: Definidas en archivos YAML que especifican el motor de consulta (ej. OpenSearch, BigQuery) y los publishers (ej. BigQuery, PubSub, Slack).
- **Ejecución**: Cada regla se ejecuta como un Kubernetes CronJob independiente para evitar fallos en cascada; soporta ejecución programada o ad-hoc.
- **Exclusiones**: Listas definidas en YAML que filtran eventos benignos usando operadores lógicos (`and`, `or`) y condiciones (regex, contains, etc.).
- **Integración LLM**: Capacidad para analizar señales de baja confianza mediante modelos de lenguaje grandes.
- **Despliegue**: Automatizado vía Helm y ConfigMaps; los cambios en las reglas desencadenan despliegues automáticos a través de CI/CD.

## Etiquetas
#ciberseguridad #kubernetes #threatdetection #helm #open

Fuente: https://github.com/nianticlabs/venator
