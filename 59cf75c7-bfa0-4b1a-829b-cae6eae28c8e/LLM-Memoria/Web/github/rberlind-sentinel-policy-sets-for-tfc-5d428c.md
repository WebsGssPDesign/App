---
fecha: 2026-10-22
etapa: aprendizaje-web
fuente: "https://github.com/rberlind/sentinel-policy-sets-for-tfc"
tema: "Terraform Sentinel Policy Sets"
tags: [web]
---
# rberlind/sentinel-policy-sets-for-tfc

## Resumen
Este repositorio alberga conjuntos de políticas Sentinel diseñados para Terraform Cloud y Enterprise, creados originalmente para una sesión técnica de septiembre de 2019. Incluye reglas específicas para AWS, Azure, GCP y VMware que limitan recursos como el tamaño de las máquinas virtuales o requieren etiquetas obligatorias. Además, proporciona casos de prueba automatizados mediante GitHub Actions para validar la efectividad de estas políticas antes de su integración.

## Datos clave
- **Cuatro conjuntos de políticas**: Uno cada uno para AWS, Azure, GCP y VMware.
- **Restricciones principales**: Limitación del tamaño de VMs (AWS/Azure/GCP), requerimiento de etiquetas específicas y control de CPU/memoria en VMware.
- **Automatización**: GitHub Actions ejecutan el Sentinel Simulator automáticamente al solicitar la fusión de cambios a la rama principal.
- **Recursos complementarios**: Diapositivas del webinar original, enlaces a grabaciones futuras y código Terraform de referencia en otro repositorio.

## Etiquetas
#TerraformCloud #Sentinel #GobernanzaInfraestructura #DevSecOps #AWS #Azure #GCP

Fuente: https://github.com/rberlind/sentinel-policy-sets-for-tfc
