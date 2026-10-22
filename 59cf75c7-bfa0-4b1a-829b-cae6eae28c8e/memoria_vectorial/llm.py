# -*- coding: utf-8 -*-
"""Cliente LLM unico. Un solo lugar con el patron: chat + quitar thinking + reintentos + metricas."""
from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

import config
import incidencias
import metricas

AQUI = Path(__file__).resolve().parent

_THINK = re.compile(r"<think(?:ing)?>.*?</think(?:ing)?>", re.S | re.I)
_SOLO_CIERRE = re.compile(r"^.*?</think(?:ing)?>", re.S | re.I)
_CERCA = re.compile(r"^```[a-zA-Z]*\n(.*)\n```$", re.S)


class ErrorLLM(RuntimeError):
    pass


class SinConexion(ErrorLLM):
    pass


class ModeloNoDisponible(ErrorLLM):
    pass


ConexionError = SinConexion


def endpoint() -> str:
    return str(config.get("llm.endpoint", "http://127.0.0.1:1234/v1")).rstrip("/")


def _cabeceras() -> dict:
    cab = {"Content-Type": "application/json"}
    clave = os.environ.get("LMSTUDIO_API_KEY") or os.environ.get("OPENAI_API_KEY") or "lm-studio"
    cab["Authorization"] = f"Bearer {clave}"
    return cab


def http_get_json(ruta: str, timeout: float = 10.0) -> dict:
    peticion = urllib.request.Request(endpoint() + ruta, headers=_cabeceras())
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise ErrorLLM(f"HTTP {e.code} en {ruta}") from e
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise SinConexion(f"sin conexion con {endpoint()}: {e}") from e
    except json.JSONDecodeError as e:
        raise ErrorLLM(f"respuesta ilegible de {ruta}") from e


def http_post_json(ruta: str, cuerpo: dict, timeout: float = 900.0) -> dict:
    datos = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
    peticion = urllib.request.Request(endpoint() + ruta, data=datos,
                                      headers=_cabeceras(), method="POST")
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", "replace")[:300]
        if e.code >= 500:
            raise SinConexion(f"HTTP {e.code}: {detalle}") from e
        raise ErrorLLM(f"HTTP {e.code}: {detalle}") from e
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise SinConexion(f"sin conexion con {endpoint()}: {e}") from e
    except json.JSONDecodeError as e:
        raise ErrorLLM("respuesta ilegible") from e


def modelos() -> list[str]:
    try:
        datos = http_get_json("/models", timeout=10.0)
    except ErrorLLM:
        return []
    salida = []
    for m in datos.get("data", []) or []:
        ident = m.get("id") or m.get("model") or ""
        if ident:
            salida.append(ident)
    return salida


def modelo_chat(preferido: str = "") -> str:
    """Orden: --model > reglas.json llm.modelo_chat > LLM_MODEL > autodeteccion > primero."""
    for candidato in (preferido, str(config.get("llm.modelo_chat", "") or "")):
        if candidato:
            return candidato
    disponibles = [m for m in modelos() if "embed" not in m.lower()]
    if not disponibles:
        return ""
    for pista in ("qwen3.5", "qwen3", "qwen"):
        for m in disponibles:
            if pista in m.lower():
                return m
    return disponibles[0]


def modelo_embed() -> str:
    for m in modelos():
        if "embed" in m.lower():
            return m
    return str(config.get("llm.modelo_embed", "") or "")


def disponible() -> bool:
    try:
        return bool(http_get_json("/models", timeout=8.0).get("data"))
    except ErrorLLM:
        return False


def limpiar_thinking(texto: str) -> str:
    if not texto:
        return ""
    limpio = _THINK.sub("", texto)
    if "</think>" in limpio.lower():
        limpio = _SOLO_CIERRE.sub("", limpio, count=1)
    return limpio.strip()


def limpiar_cerca(texto: str) -> str:
    m = _CERCA.match((texto or "").strip())
    return m.group(1).strip() if m else (texto or "").strip()


def prompt(nombre: str, por_defecto: str = "") -> str:
    """Lee prompts/<nombre>.md. Si no existe, usa el texto de respaldo."""
    if not config.get("prompts.usar_disco", True):
        return por_defecto
    ruta = AQUI / str(config.get("prompts.dir", "prompts")) / f"{nombre}.md"
    try:
        texto = ruta.read_text(encoding="utf-8").strip()
        return texto or por_defecto
    except OSError:
        return por_defecto


def esperar_modelo(stop_path=None, maximo: int = 3600) -> str:
    """Espera a que haya un modelo de chat. Devuelve '' si se pidio parar."""
    stop = Path(stop_path) if stop_path else None
    inicio = time.time()
    while not (stop and stop.exists()):
        m = modelo_chat()
        if m:
            return m
        if time.time() - inicio > maximo:
            return ""
        for _ in range(12):
            if stop and stop.exists():
                return ""
            time.sleep(5)
    return ""


def chat(sistema: str = "", usuario: str = "", modelo: str = "",
         temperature: float | None = None, max_tokens: int | None = None,
         timeout: float | None = None, sin_thinking: bool = True,
         etapa: str = "llm", etiqueta: str = "") -> str:
    modelo = modelo or modelo_chat()
    if not modelo:
        raise ModeloNoDisponible("no hay modelo de chat cargado en LM Studio")

    mensajes = []
    if sistema:
        mensajes.append({"role": "system", "content": sistema})
    mensajes.append({"role": "user", "content": usuario})

    cuerpo = {
        "model": modelo,
        "messages": mensajes,
        "temperature": float(temperature if temperature is not None else config.get("llm.temperature", 0.2)),
        "max_tokens": int(max_tokens if max_tokens is not None else config.get("llm.max_tokens", 1500)),
        "stream": False,
    }
    if sin_thinking:
        cuerpo["chat_template_kwargs"] = {"enable_thinking": False}

    intentos = max(1, int(config.get("llm.reintentos", 3)))
    pausa = float(config.get("llm.pausa_reintento", 5.0))
    espera = float(timeout if timeout is not None else config.get("llm.timeout", 900))
    t0 = time.time()
    ultimo: Exception | None = None

    for i in range(intentos):
        try:
            datos = http_post_json("/chat/completions", cuerpo, timeout=espera)
            texto = (datos["choices"][0]["message"].get("content") or "")
            metricas.registrar(etapa, etiqueta, time.time() - t0, len(usuario), len(texto), "ok", modelo)
            return limpiar_thinking(texto) if sin_thinking else texto
        except SinConexion as e:
            ultimo = e
            if i < intentos - 1:
                time.sleep(pausa * (i + 1))
        except (ErrorLLM, KeyError, IndexError) as e:
            ultimo = e
            if i < intentos - 1:
                time.sleep(1.5 * (i + 1))

    metricas.registrar(etapa, etiqueta, time.time() - t0, len(usuario), 0, "error", modelo)
    incidencias.registrar_si_toca("llm", type(ultimo).__name__, "media", str(ultimo)[:200])
    raise ultimo if ultimo else ErrorLLM("fallo desconocido")


def main() -> int:
    import sys
    if "--check" in sys.argv:
        print(f"endpoint      : {endpoint()}")
        print(f"disponible    : {disponible()}")
        print(f"modelos       : {modelos()}")
        print(f"modelo_chat   : {modelo_chat() or 'NINGUNO'}")
        print(f"modelo_embed  : {modelo_embed() or 'NINGUNO'}")
        print(f"prompts dir   : {AQUI / str(config.get('prompts.dir', 'prompts'))}")
        print(f"limpiar_test  : {limpiar_thinking('a</think>b')!r}")
        return 0
    print(chat("Responde solo: ok", "Hola"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
