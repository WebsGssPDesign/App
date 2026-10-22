---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/1208.2724v5"
tema: "React Server Actions Caching"
tags: [web]
---
# Caching with rental cost and zapping

## Resumen
Este artículo analiza el problema de caché de archivos bajo dos variantes: con costo de alquiler y con "zapping". El objetivo es minimizar los costos totales de recuperación, alquiler y zapping mediante algoritmos online deterministas y aleatorizados. Se presentan cotas competitivas para estos modelos y se extienden algoritmos existentes de cobertura online.

## Datos clave
- **Caché con costo de alquiler**: Implica un costo $λ$ por unidad de tiempo para cada archivo en la caché; se minimiza la suma de costos de recuperación y alquiler.
- **Caché con zapping**: Permite "zapear" un archivo pagando un costo $N$, eliminando futuros costos de acceso a ese archivo específico.
- **Combinación híbrida**: Se estudia una variante que integra tanto el costo de alquiler como el de zapping.
- **Algoritmos online**: Se desarrollan y extienden algoritmos deterministas y aleatorizados dentro del marco de análisis competitivo para establecer cotas inferiores y superiores.

## Etiquetas
#caché #optimización_online #algoritmos_deterministas #costos_de_alquiler #zapping

Fuente: http://arxiv.org/abs/1208.2724v5
