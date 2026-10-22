---
fecha: 2026-10-20
etapa: aprendizaje-web
fuente: "http://arxiv.org/abs/2608.02672v1"
tema: "Terraform Sentinel"
tags: [web]
---
# Security-First Evaluation of Text-to-Terraform: Benchmarking LLMs and SLMs for Secure IaC Generation

## Resumen
El estudio evalúa la capacidad de siete modelos (LLMs y SLMs) para generar código Terraform seguro en 17 escenarios, integrando escáneres Checkov y Trivy en una pipeline CI/CD. Se concluye que la validez sintáctica y el cumplimiento de seguridad son propiedades ortogonales: un modelo puede generar código bien formado pero inseguro. La ingeniería de prompts por sí sola es insuficiente; se requiere necesariamente el uso complementario de escaneo automatizado multi-herramienta para garantizar IaC seguro, independientemente del modelo o estrategia utilizada.

## Datos clave
- **Modelos evaluados**: 3 LLMs cerrados (Claude Opus 4, GPT-5.4, Gemini 2.5 Pro) y 4 SLMs abiertos (Qwen2.5-Coder-14B, WizardCoder-33B, CodeLlama-13B, Magicoder-S-CL-7B).
- **Escenarios**: 17 casos de uso en AWS Terraform.
- **Herramientas de seguridad**: Checkov y Trivy integrados en GitLab CI/CD.
- **Métrica clave**: WizardCoder-33B logró un 77.8% de validación sintáctica pero 0% de cumplimiento Checkov; Claude Opus 4 alcanzó 23.1% (Checkov) y 92.5% (Trivy).
- **Estrategia**: Evaluación con dos estrategias de prompt a tres niveles de seguridad (pass@5).

## Etiquetas
#InfraestructuraComoCodigo #SeguridadCiberseguridad #IAGenerativa #Terraform #DevSecOps

Fuente: http://arxiv.org/abs/2608.02672v1
