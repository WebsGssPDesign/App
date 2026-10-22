# -*- coding: utf-8 -*-
"""Configuracion unica del sistema.

Precedencia (menor a mayor):
    1. DEFAULTS de este archivo
    2. Sistema/reglas.json
    3. variables de entorno   (SECCION_CLAVE, p. ej. MEMORIA_MIN_SIM)

Nunca lanza por un reglas.json corrupto: cae a DEFAULTS y sigue.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

AQUI = Path(__file__).resolve().parent

_ALIAS_ENV = {
    "rutas.boveda": "MEMORIA_BOVEDA",
    "rutas.notas": "MEMORIA_NOTAS",
    "rutas.skills": "MEMORIA_SKILLS",
    "llm.modelo_chat": "LLM_MODEL",
    "llm.endpoint": "LMSTUDIO_URL",
}

DEFAULTS: dict[str, Any] = {
    "version": 1,
    "rutas": {
        "boveda": r"F:\automatizaciones\homeLab",
        "notas": "LLM-Memoria",
        "diario": "Diario",
        "skills": "skills",
        "papelera": "Sistema/papelera",
        "descartados": "_descartados",
    },
    "llm": {
        "endpoint": "http://127.0.0.1:1234/v1",
        "modelo_chat": "",
        "modelo_embed": "",
        "timeout": 900,
        "reintentos": 3,
        "pausa_reintento": 5.0,
        "temperature": 0.2,
        "max_tokens": 1500,
    },
    "memoria": {
        "min_sim": 0.35, "pool": 30, "chunk_chars": 1200, "overlap": 150,
        "batch": 32, "lock_vencimiento": 900, "max_sync_segundos": 25,
        "max_caracteres_resultado": 800, "max_caracteres_total": 4000, "timeout": 120,
    },
    "aprender": {
        "max_chars": 6000, "max_tokens": 1500, "temperature": 0.2, "timeout": 900,
        "max_intentos": 3, "pausa": 0.5, "max_minutos": 480, "sin_conexion_seg": 1800,
        "excluir": ["LLM-Memoria", "Diario", "memoria_vectorial", ".memoria", "assets",
                    ".venv", "node_modules", ".git", ".obsidian", ".trash", "papelera"],
        "extensiones": [".md", ".txt"],
    },
    "skills": {
        "max_por_corrida": 8, "min_material": 3, "rondas_vacias": 2, "reintentar_dias": 14,
        "max_tokens": 600,
        "secciones": ["## Proposito", "## Cuando usarla", "## Pasos", "## Reglas",
                      "## Errores comunes", "## Fuentes"],
    },
    "web": {
        "fuentes_api": ["wikipedia", "arxiv", "github"],
        "fuentes_html": ["react.dev", "nextjs.org", "python.org", "docs.n8n.io",
                         "learn.microsoft.com", "nodejs.org", "sqlite.org", "obsidian.md"],
        "respetar_robots": True, "min_texto": 600, "max_texto": 6000,
        "max_bytes": 2000000, "pausa_ciclo_seg": 300,
        "min_relevancia": 0.45, "min_prioridad": 0.25,
        "enfriamiento_min": 15, "fallos_para_aislar": 5, "horas_aislamiento": 24,
        "dominios_permitidos": ["react.dev", "nextjs.org", "mongodb.com", "python.org",
                                "developer.mozilla.org", "wikipedia.org", "arxiv.org",
                                "github.com", "docs.n8n.io", "learn.microsoft.com"],
        "dominios_prohibidos": ["pinterest.com", "quora.com"],
        "limites": {"max_por_hora": 30, "max_por_dia": 200, "max_bytes_dia": 20000000},
    },
    "indice": {
        "extensiones": [".md", ".txt", ".py", ".js", ".ts", ".jsx", ".tsx", ".json", ".yml",
                        ".yaml", ".toml", ".ini", ".cfg", ".ps1", ".bat", ".sh", ".sql",
                        ".css", ".html"],
        "ignorar_archivos": ["Progreso.md", "Tablero.md", "AprendidoHoy.md",
                             "AprendidoSemana.md", "Cola.md", "heartbeat.json",
                             "incidencias.json", "metricas.jsonl", "auditoria.jsonl",
                             "eventos.jsonl", "descartes.jsonl"],
        "ignorar_dirs": ["LLM-Memoria/MOC", "LLM-Memoria/Revision", "memoria_vectorial",
                         ".memoria", ".venv", "node_modules", ".git", ".obsidian",
                         ".trash", "_descartados", "Sistema/papelera", "assets"],
        "max_bytes_archivo": 300000,
        "watch_segundos": 20,
    },
    "guardian": {
        "activo": True, "modo": "observacion",
        "vigilar": ["lmstudio", "sqlite", "indice", "heartbeat", "incidencias",
                    "locks", "logs", "deps", "disco"],
        "intervalo_segundos": 60, "cooldown_min": 10, "max_reparaciones_hora": 6,
        "permitir_pip": True, "permitir_reiniciar_lmstudio": True,
        "permitir_escribir_codigo": False, "verificar_integridad_min": 60,
        "backup_dias": 7, "heartbeat_vencido_seg": 300, "guardian_vencido_seg": 300,
        "espacio_minimo_gb": 5, "log_max_mb": 5, "deps_verificar": True,
        "cooldown_incidencia_min": 15,
        "reparaciones_permitidas": ["lock_obsoleto", "log_rotado", "servidor_lmstudio",
                                    "pip_faltantes", "indice_corrupto", "backup",
                                    "heartbeat_colgado"],
    },
    "eventos": {"activo": True, "webhook": "", "timeout": 5},
    "prompts": {"dir": "prompts", "usar_disco": True},
    "tablero": {"dias_grafico": 30, "min_notas_moc": 3,
                "repaso_dias": [1, 3, 7, 21, 60], "max_listado": 25},
    "confianza": {"por_fuente": {"oficial": "alta", "arxiv": "alta", "local": "alta",
                                 "wikipedia": "media", "github": "media", "sistema": "media",
                                 "blog": "baja", "stackoverflow": "media"}},
    "agente": {"idioma": "es", "inferir_stack": True, "avisar_datos_no_instrucciones": True},
}

_cache: dict | None = None
_cache_mtime: float = -1.0


def boveda() -> Path:
    return Path(os.environ.get("MEMORIA_BOVEDA") or DEFAULTS["rutas"]["boveda"])


def ruta_reglas() -> Path:
    return boveda() / "Sistema" / "reglas.json"


def _fusionar(base: dict, encima: dict) -> dict:
    salida = dict(base)
    for k, v in encima.items():
        if k.startswith("_"):
            continue
        if isinstance(v, dict) and isinstance(salida.get(k), dict):
            salida[k] = _fusionar(salida[k], v)
        else:
            salida[k] = v
    return salida


def _default_de(clave: str) -> Any:
    valor: Any = DEFAULTS
    for parte in clave.split("."):
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            return None
    return valor


def cargar(recargar: bool = False) -> dict:
    global _cache, _cache_mtime
    ruta = ruta_reglas()
    try:
        mtime = ruta.stat().st_mtime
    except OSError:
        mtime = -1.0
    if _cache is not None and not recargar and mtime == _cache_mtime:
        return _cache
    datos: dict = {}
    if mtime >= 0:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                crudo = json.load(f)
            if isinstance(crudo, dict):
                datos = crudo
        except (OSError, json.JSONDecodeError):
            datos = {}
    _cache = _fusionar(DEFAULTS, datos)
    _cache_mtime = mtime
    return _cache


def _env_de(clave: str) -> str | None:
    alias = _ALIAS_ENV.get(clave)
    if alias and os.environ.get(alias) not in (None, ""):
        return os.environ[alias]
    return os.environ.get(clave.replace(".", "_").upper())


def _convertir(texto: str, referencia: Any) -> Any:
    if isinstance(referencia, bool):
        return texto.strip().lower() in ("1", "true", "si", "sí", "yes", "on")
    if isinstance(referencia, int) and not isinstance(referencia, bool):
        try:
            return int(texto)
        except ValueError:
            return referencia
    if isinstance(referencia, float):
        try:
            return float(texto)
        except ValueError:
            return referencia
    if isinstance(referencia, list):
        return [p.strip() for p in texto.split(",") if p.strip()]
    return texto


def get(clave: str, por_defecto: Any = None) -> Any:
    valor = cargar()
    for parte in clave.split("."):
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            valor = _default_de(clave) if por_defecto is None else por_defecto
            break
    env = _env_de(clave)
    if env is not None:
        return _convertir(env, valor)
    return valor


def seccion(nombre: str) -> dict:
    datos = dict(cargar().get(nombre, {}))
    for clave in list(datos):
        if clave.startswith("_"):
            datos.pop(clave)
            continue
        env = _env_de(f"{nombre}.{clave}")
        if env is not None:
            datos[clave] = _convertir(env, datos[clave])
    return datos


def origen(clave: str) -> str:
    if _env_de(clave) is not None:
        return "env"
    crudo: Any = cargar()
    for parte in clave.split("."):
        if isinstance(crudo, dict) and parte in crudo:
            crudo = crudo[parte]
        else:
            return "default"
    return "reglas.json"


# ------------------------------------------------------------------ rutas
VAULT = boveda()
SISTEMA = VAULT / "Sistema"
PERFIL = VAULT / "Perfil"
MEM_DIR = VAULT / str(get("rutas.notas"))
HECHOS = MEM_DIR / "Hechos"
WEB_DIR = MEM_DIR / "Web"
SKILLS_DIR = VAULT / str(get("rutas.skills"))
DIARIO = VAULT / str(get("rutas.diario"))
PAPELERA = VAULT / str(get("rutas.papelera"))
DESCARTADOS = VAULT / str(get("rutas.descartados"))
ESTADO_DIR = VAULT / ".memoria"

RUTAS_ESCRIBIBLES = (MEM_DIR, SKILLS_DIR, DIARIO, PERFIL, SISTEMA)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--check" not in argv:
        print(__doc__)
        return 0
    claves = [
        "rutas.boveda", "rutas.notas", "memoria.min_sim", "memoria.pool",
        "memoria.max_sync_segundos", "aprender.max_chars", "aprender.excluir",
        "web.dominios_permitidos", "web.limites.max_por_hora", "indice.ignorar_archivos",
        "guardian.activo", "guardian.permitir_escribir_codigo", "tablero.repaso_dias",
    ]
    print(f"reglas.json : {ruta_reglas()}  ({'presente' if ruta_reglas().exists() else 'AUSENTE -> defaults'})")
    for clave in claves:
        valor = get(clave)
        if isinstance(valor, list):
            valor = f"[{len(valor)} elementos]"
        print(f"  {clave:<34} = {valor!r:<28} origen={origen(clave)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
