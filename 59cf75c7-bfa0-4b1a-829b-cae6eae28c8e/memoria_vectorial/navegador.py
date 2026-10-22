# -*- coding: utf-8 -*-
"""Navegador HTTP educado. Sin dependencias externas."""
from __future__ import annotations

import gzip
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

import config
import incidencias
import memoria
from util import ahora, append_linea, atomic_write_json, bloqueo, leer_json

CACHE = config.SISTEMA / "cache_web"
PACING = config.SISTEMA / ".pacing.json"
LOCK = config.SISTEMA / ".navegador.lock"
UA = "Mozilla/5.0 (compatible; homeLab-memoria/1.0)"
DEFAULT_ESPERA = 1.5
ROBOTS_TTL = 86400


def dominio_de(url: str) -> str:
    try:
        return (urllib.parse.urlparse(url).hostname or "").lower()
    except ValueError:
        return ""


def permitido(url: str) -> tuple[bool, str]:
    d = dominio_de(url)
    if not d:
        return False, "sin dominio"
    permitidos = [x.lower() for x in config.get("web.dominios_permitidos", [])]
    prohibidos = [x.lower() for x in config.get("web.dominios_prohibidos", [])]
    if any(d == p or d.endswith("." + p) for p in prohibidos):
        return False, f"dominio prohibido: {d}"
    if permitidos and not any(d == p or d.endswith("." + p) for p in permitidos):
        return False, f"fuera de la lista blanca: {d}"
    return True, ""


def _sha(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:20]


def _robots_ruta(dominio: str) -> Path:
    return CACHE / "_robots" / f"{dominio}.json"


def _robots(dominio: str) -> dict:
    ruta = _robots_ruta(dominio)
    datos = leer_json(ruta, None)
    if isinstance(datos, dict) and time.time() - float(datos.get("ts", 0)) < ROBOTS_TTL:
        return datos
    reglas = {"ts": time.time(), "disallow": [], "allow": [], "crawl_delay": None, "error": ""}
    if config.get("web.respetar_robots", True):
        try:
            texto = _bajar(f"https://{dominio}/robots.txt", timeout=10, condicional=False)
            for linea in (texto or "").splitlines():
                linea = linea.split("#")[0].strip()
                if not linea or ":" not in linea:
                    continue
                clave, valor = (p.strip() for p in linea.split(":", 1))
                clave = clave.lower()
                if clave == "disallow" and valor:
                    reglas["disallow"].append(valor)
                elif clave == "allow" and valor:
                    reglas["allow"].append(valor)
                elif clave == "crawl-delay":
                    try:
                        reglas["crawl_delay"] = float(valor)
                    except ValueError:
                        pass
        except Exception as e:
            reglas["error"] = str(e)[:120]
    atomic_write_json(ruta, reglas)
    return reglas


def _coincide(patron: str, ruta: str) -> bool:
    if patron in ("", "/"):
        return True
    if patron.endswith("*"):
        return ruta.startswith(patron[:-1])
    return ruta.startswith(patron)


def robots_permite(url: str) -> bool:
    if not config.get("web.respetar_robots", True):
        return True
    partes = urllib.parse.urlparse(url)
    ruta = partes.path or "/"
    reglas = _robots(partes.hostname or "")
    for patron in reglas.get("allow", []):
        if _coincide(patron, ruta):
            return True
    for patron in reglas.get("disallow", []):
        if _coincide(patron, ruta):
            return False
    return True


def _esperar_turno(dominio: str) -> None:
    reglas = _robots(dominio)
    espera = reglas.get("crawl_delay") or DEFAULT_ESPERA
    espera = max(0.5, min(float(espera), 15.0))
    with bloqueo(LOCK, vencimiento=30) as mio:
        if not mio:
            time.sleep(espera)
            return
        datos = leer_json(PACING, {})
        ultimo = float(datos.get(dominio, 0))
        falta = espera - (time.time() - ultimo)
        if falta > 0:
            time.sleep(falta)
        datos[dominio] = time.time()
        atomic_write_json(PACING, datos)


def presupuesto_ok() -> tuple[bool, str]:
    limites = config.seccion("web").get("limites", {}) or {}
    hora = memoria.contador_leer("web.hora", ventana_horas=1)
    dia = memoria.contador_leer("web.dia", ventana_horas=24)
    if hora >= int(limites.get("max_por_hora", 30)):
        return False, f"limite por hora alcanzado ({hora})"
    if dia >= int(limites.get("max_por_dia", 200)):
        return False, f"limite diario alcanzado ({dia})"
    return True, ""


def _consumir(nbytes: int) -> None:
    memoria.contador_sumar("web.hora", 1, ventana_horas=1)
    memoria.contador_sumar("web.dia", 1, ventana_horas=24)
    memoria.contador_sumar("web.bytes_dia", nbytes, ventana_horas=24)


def _cache_ruta(url: str) -> Path:
    return CACHE / f"{_sha(url)}.json"


def leer_cache(url: str) -> dict | None:
    datos = leer_json(_cache_ruta(url), None)
    return datos if isinstance(datos, dict) else None


def _guardar_cache(url: str, texto: str, titulo: str, etag: str, lm: str) -> None:
    atomic_write_json(_cache_ruta(url), {
        "url": url, "fecha": ahora(), "etag": etag, "last_modified": lm,
        "sha": _sha(texto), "titulo": titulo, "texto": texto,
    })


def _bajar(url: str, timeout: float = 30.0, condicional: bool = True) -> str:
    previo = leer_cache(url) if condicional else None
    cabeceras = {"User-Agent": UA,
                 "Accept": "text/html,application/xhtml+xml,application/json,*/*",
                 "Accept-Encoding": "gzip"}
    if previo:
        if previo.get("etag"):
            cabeceras["If-None-Match"] = previo["etag"]
        if previo.get("last_modified"):
            cabeceras["If-Modified-Since"] = previo["last_modified"]
    req = urllib.request.Request(url, headers=cabeceras)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            crudo = r.read(int(config.get("web.max_bytes", 2000000)))
            if r.headers.get("Content-Encoding") == "gzip":
                crudo = gzip.decompress(crudo)
            return crudo.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code == 304 and previo:
            return previo.get("texto", "")
        if e.code == 429:
            incidencias.registrar("web", "429 demasiadas peticiones", "media", dominio_de(url))
        raise


class _Extractor(HTMLParser):
    BLOQUE = {"script", "style", "nav", "footer", "header", "aside", "noscript", "svg",
              "form", "iframe"}
    SALTO = {"p", "div", "section", "article", "li", "tr", "br", "h1", "h2", "h3", "h4",
             "h5", "pre"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._saltar = 0
        self._pre = 0
        self._titulo = False
        self.trozos: list[str] = []
        self.titulo = ""

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOQUE:
            self._saltar += 1
        elif tag == "title":
            self._titulo = True
        elif tag == "pre":
            self._pre += 1
        elif tag in self.SALTO:
            self.trozos.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BLOQUE and self._saltar:
            self._saltar -= 1
        elif tag == "title":
            self._titulo = False
        elif tag == "pre" and self._pre:
            self._pre -= 1
        elif tag in self.SALTO:
            self.trozos.append("\n")

    def handle_data(self, data):
        if self._titulo:
            self.titulo += data
        if self._saltar or not data.strip():
            return
        self.trozos.append(data if self._pre else re.sub(r"\s+", " ", data))


def extraer(html: str) -> tuple[str, str]:
    p = _Extractor()
    try:
        p.feed(html)
    except Exception:
        pass
    texto = "".join(p.trozos)
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto).strip()
    return texto, re.sub(r"\s+", " ", p.titulo).strip()


def sitemap(dominio: str, maximo: int = 200) -> list[str]:
    urls: list[str] = []
    for candidato in (f"https://{dominio}/sitemap.xml", f"https://{dominio}/sitemap_index.xml"):
        try:
            xml = _bajar(candidato, timeout=20, condicional=False)
        except Exception:
            continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml or "", flags=re.I)
        if not locs:
            continue
        if any(l.lower().endswith(".xml") for l in locs[:5]):
            for sub in locs[:5]:
                try:
                    xml2 = _bajar(sub, timeout=20, condicional=False)
                    urls += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml2 or "", flags=re.I)
                except Exception:
                    continue
        else:
            urls += locs
        if urls:
            break
    vistos, salida = set(), []
    for u in urls:
        if u not in vistos:
            vistos.add(u)
            salida.append(u)
        if len(salida) >= maximo:
            break
    return salida


def descubrir(dominio: str, palabras: list[str], maximo: int = 5) -> list[str]:
    palabras = [p.lower().replace(" ", "-") for p in palabras if p]
    puntuadas = []
    for u in sitemap(dominio):
        ruta = urllib.parse.urlparse(u).path.lower()
        if any(x in ruta for x in ("/blog/", "/changelog", "/pricing", "/careers", "/legal", "/404")):
            continue
        punt = sum(2 if p in ruta else 0 for p in palabras)
        punt -= len(ruta.split("/")) * 0.1
        puntuadas.append((punt, u))
    puntuadas.sort(key=lambda x: -x[0])
    return [u for _, u in puntuadas[:maximo]]


def obtener(url: str, max_caracteres: int = 0) -> dict:
    """Devuelve {ok, url, texto, titulo, motivo}. Nunca lanza."""
    ok, motivo = permitido(url)
    if not ok:
        return {"ok": False, "url": url, "motivo": motivo}
    ok, motivo = presupuesto_ok()
    if not ok:
        return {"ok": False, "url": url, "motivo": motivo}
    if not robots_permite(url):
        return {"ok": False, "url": url, "motivo": "robots.txt lo prohibe"}

    _esperar_turno(dominio_de(url))
    try:
        crudo = _bajar(url)
    except Exception as e:
        incidencias.registrar_si_toca("web", type(e).__name__, "baja", dominio_de(url))
        return {"ok": False, "url": url, "motivo": f"{type(e).__name__}: {str(e)[:120]}"}

    _consumir(len(crudo))
    if crudo.lstrip().startswith(("{", "[")):
        texto, titulo = crudo, ""
    else:
        texto, titulo = extraer(crudo)
    if len(texto) < int(config.get("web.min_texto", 600)):
        return {"ok": False, "url": url, "motivo": f"texto pobre ({len(texto)} caracteres)"}

    texto = texto[: max_caracteres or int(config.get("web.max_texto", 6000))]
    _guardar_cache(url, texto, titulo, "", "")
    return {"ok": True, "url": url, "texto": texto, "titulo": titulo, "motivo": ""}


def descartar(url: str, motivo: str, detalle: str = "") -> None:
    try:
        append_linea(config.SISTEMA / "descartes.jsonl", json.dumps(
            {"fecha": ahora(), "url": url, "motivo": motivo, "detalle": detalle[:200]},
            ensure_ascii=False))
    except OSError:
        pass


def main() -> int:
    import sys
    if "--check" in sys.argv:
        print(f"cache        : {CACHE}")
        print(f"permitidos   : {len(config.get('web.dominios_permitidos', []))}")
        print(f"presupuesto  : {presupuesto_ok()}")
        for u in config.get("web.dominios_permitidos", [])[:3]:
            print(f"  {u}: robots={'si' if robots_permite('https://' + u + '/') else 'no'}")
        return 0
    url = sys.argv[1] if len(sys.argv) > 1 else "https://react.dev/learn"
    r = obtener(url)
    print({k: (v[:300] + "..." if k == "texto" and len(v) > 300 else v) for k, v in r.items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
