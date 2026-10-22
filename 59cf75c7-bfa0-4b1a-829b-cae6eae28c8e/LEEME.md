# Paquete memoria_vectorial

Generado para Guillermo Samuel Simones Primera. Contenido de los bloques A, B, C y D.

## Estructura

```
homeLab/
├─ INSTALAR.ps1              <- copia todo a su sitio, con backups
├─ AGENTS.md                 <- va en la RAIZ de la boveda
├─ Sistema/reglas.json       <- va en Sistema/
├─ Perfil/*.json             <- van en Perfil/
└─ memoria_vectorial/        <- va en memoria_vectorial/
   ├─ (modulos nuevos .py)
   ├─ prompts/*.md
   ├─ tests/*.py
   ├─ README.md
   ├─ requirements.txt
   ├─ requirements-dev.txt
   └─ PARCHES/*.md           <- instrucciones para los archivos que YA TENIAS
```

## Que es archivo nuevo y que es parche

**Archivos completos** (se copian tal cual, no existian antes):

config.py, util.py, heartbeat.py, incidencias.py, metricas.py, perfil.py, escritor.py,
llm.py, eventos.py, guardian.py, navegador.py, analisis.py, entidades.py, tablero.py,
estado.py, README.md, requirements.txt, requirements-dev.txt, prompts/, tests/,
Perfil/*.json, Sistema/reglas.json, AGENTS.md

**Parches** (instrucciones exactas, porque el archivo ya existia):

memoria.py, iniciar.ps1, aprender.py, crear_skills.py, aprender_web.py, indexer.py,
mcp_server.py

Los parches estan en `memoria_vectorial/PARCHES/`. Cada uno dice que funcion reemplazar
y por cual. Lee el LEEME de esa carpeta antes de empezar.

## Orden recomendado

1. `INSTALAR.ps1` copia los archivos completos (hace .bak de lo que pise).
2. Aplicar los parches en el orden indicado en PARCHES/00-leeme.md.
3. `python -m pytest tests -q` — deben pasar los 26 tests.
4. `python config.py --check` y `python perfil.py --check`.
5. `python guardian.py --una-vez` en modo observacion.

## Aviso

`estado.py` viene como archivo completo porque se reescribio entero: haz `.bak` del tuyo
antes de pisarlo si le habias anadido algo.
