---
fecha: 2026-10-21
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2608.24601v1"
tema: "PostgreSQL Query Pushdown"
tags: [web]
---
# Pushdown Model Checking Above the Cubic Bottleneck

## Resumen
Este estudio analiza por qué no existen algoritmos más rápidos que los existentes para el problema de comprobación de modelos en autómatas con pila (PDA). Los autores demuestran, bajo ciertas hipótesis de complejidad fina, que es improbable superar la barrera cúbica actual. Además, proponen una nueva hipótesis llamada 2NPDA(k) para explicar las limitaciones en algoritmos basados en el tamaño total del input.

## Datos clave
- **Complejidad conocida**: $O(n^{2k} |Σ| + n^{3k})$, donde $n$ es el número de estados y $k$ la cantidad de NFAs.
- **Hipótesis 3k-Clique**: Si es cierta, impide algoritmos más rápidos que $O((n^{(ω-1)k} |Σ| + n^{ωk})^{1-ε})$.
- **Hipótesis combinatoria 3k-Clique**: Impide resolver el problema en menos de $O(n^{3(k-1)-ε})$ para alfabetos constantes.
- **Hipótesis 2NPDA(k)**: Nueva hipótesis propuesta para explicar la falta de algoritmos $O(N^{3k-ε})$, donde $N$ es el tamaño total del input en bits.
- **Reducciones lineales**: Se establece una red de reducciones entre esta nueva hipótesis y otros problemas de teoría de autómatas.

## Etiquetas
#verificación #autómatas #complejidad_fina #hipótesis_2NPDA

Fuente: http://arxiv.org/abs/2608.24601v1
