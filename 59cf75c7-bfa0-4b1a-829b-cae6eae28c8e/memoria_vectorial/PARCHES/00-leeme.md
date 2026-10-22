# Parches

Estos archivos YA LOS TENIAS. Aqui van las instrucciones exactas para modificarlos.
Cada parche dice que funcion reemplazar y por cual. No reescribas el archivo entero.

## Orden recomendado

1. `memoria.py`  — es el nucleo, y los demas dependen de sus nombres nuevos
2. `iniciar.ps1`
3. `indexer.py`
4. `aprender.py`
5. `crear_skills.py`
6. `aprender_web.py`
7. `mcp_server.py`

Antes de empezar, haz copia:

```powershell
Copy-Item memoria.py memoria.py.original
Copy-Item iniciar.ps1 iniciar.ps1.original
```

Despues de cada parche, ejecuta `python -m pytest tests -q`. Si algo se rompe, restauras
el `.original` y avisas.

## Regla de oro

Ninguna constante cambia de valor por defecto. Los parches solo las mueven a `config.get`,
que respeta las variables de entorno que ya usabas. Si algo cambia de comportamiento
observable, es un bug del parche.
