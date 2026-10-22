---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2410.22919v3"
tema: "WebAssembly Streaming"
tags: [web]
---
# Cyber-physical WebAssembly: Secure Hardware Interfaces and Pluggable Drivers

## Resumen
Este documento propone el uso de WebAssembly y la interfaz WASI para facilitar la interacción segura con hardware en entornos IoT y dispositivos embebidos. Se presentan implementaciones conceptuales que permiten a las aplicaciones ejecutar controladores nativos directamente dentro del entorno WebAssembly para protocolos como I2C y USB. La evaluación indica una sobrecarga mínima de hasta un 8% respecto a las APIs nativas, aunque advierte sobre posibles retrasos significativos durante la inicialización en aplicaciones de baja latencia.

## Datos clave
- Protocolos soportados: I2C y USB.
- Tecnología central: WebAssembly System Interface (WASI).
- Sobrecarga máxima observada: 8% comparado con APIs nativas del sistema operativo.
- Desafío crítico: La sobrecarga de inicialización en tiempo de ejecución afecta aplicaciones de baja latencia.
- Beneficio principal: Permite actualizar y gestionar configuraciones complejas en dispositivos heterogéneos con mayor facilidad que los métodos tradicionales.

## Etiquetas
#WebAssembly #IoT #Ciberfísica #Seguridad #WASI

Fuente: http://arxiv.org/abs/2410.22919v3
