---
fecha: 2026-10-20
etapa: aprendizaje
fuente: "Context/emprendimientos/.md/guia-desarrollo-juego-goii.md"
tags: [hecho]
---
# guia-desarrollo-juego-goii.md

## Resumen
Esta guía detalla el desarrollo de un juego de estrategia espacial asincrónico utilizando Godot 4.x para el cliente y Node.js/PostgreSQL para el backend. Su objetivo es establecer una arquitectura segura donde el servidor valide todas las acciones, evitando manipulaciones por parte del jugador.

## Datos clave
- **Tecnologías**: Godot 4.x (GDScript), Node.js + Express, PostgreSQL (o SQLite), LM Studio con Qwen3-Coder.
- **Modelo de datos**: Estructuras JSON para datos estáticos (`edificios.json`, `naves.json`) y tablas dinámicas en BD para estado del jugador (`jugador`, `base_jugador`, `cola_construccion`).
- **Backend**: API REST con endpoints críticos: `/estado` (lectura), `/construir`, `/investigar`, `/recolectar` (cálculo de recursos offline) y `/atacar`.
- **Cliente**: Arquitectura basada en escenas (`Base.tscn`, `MapaGalaxia.tscn`) y un singleton `ApiClient.gd` para centralizar llamadas HTTP.
- **Flujo**: Diseño previo de reglas, implementación del backend como autoridad única, y construcción progresiva de interfaces visuales.

## Etiquetas
#Godot4 #JuegoEstrategia #BackendNodeJS #DesarrolloGamedev

Fuente: `F:\automatizaciones\homeLab\Context\emprendimientos\.md\guia-desarrollo-juego-goii.md`
