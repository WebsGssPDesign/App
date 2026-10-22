# -*- coding: utf-8 -*-
"""Utilidades compartidas: escritura atomica, JSON tolerante y bloqueos entre procesos."""
from __future__ import annotations

import contextlib
import json
import os
import time
from pathlib import Path
from typing import Any, Iterator


def ahora() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def hoy() -> str:
    return time.strftime("%Y-%m-%d")


def atomic_write_text(destino: Path, texto: str, encoding: str = "utf-8") -> None:
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_name(destino.name + ".tmp")
    with open(tmp, "w", encoding=encoding, newline="\n") as f:
        f.write(texto)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, destino)


def atomic_write_json(destino: Path, datos: Any, indent: int = 2) -> None:
    atomic_write_text(destino, json.dumps(datos, ensure_ascii=False, indent=indent) + "\n")


def append_linea(destino: Path, linea: str) -> None:
    """Append de una sola linea (jsonl). Un unico os.write: seguro entre procesos."""
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(destino), os.O_CREAT | os.O_WRONLY | os.O_APPEND, 0o644)
    try:
        os.write(fd, (linea.rstrip("\n") + "\n").encode("utf-8"))
    finally:
        os.close(fd)


def leer_json(ruta: Path, por_defecto: Any) -> Any:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return por_defecto


def leer_lineas_json(ruta: Path, maximo: int = 0) -> list[dict]:
    salida: list[dict] = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    salida.append(json.loads(linea))
                except json.JSONDecodeError:
                    continue
    except OSError:
        return []
    return salida[-maximo:] if maximo else salida


def edad_segundos(ruta: Path) -> float:
    try:
        return max(0.0, time.time() - Path(ruta).stat().st_mtime)
    except OSError:
        return float("inf")


def proceso_vivo(pid: int) -> bool:
    if pid <= 0:
        return False
    if os.name == "nt":
        # os.kill() no funciona en Windows (lanza SystemError): usar ctypes.
        import ctypes
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        STILL_ACTIVE = 259
        ERROR_ACCESS_DENIED = 5
        kernel32 = ctypes.windll.kernel32
        h = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, int(pid))
        if not h:
            return kernel32.GetLastError() == ERROR_ACCESS_DENIED
        try:
            codigo = ctypes.c_ulong()
            if kernel32.GetExitCodeProcess(h, ctypes.byref(codigo)):
                return codigo.value == STILL_ACTIVE
            return True
        finally:
            kernel32.CloseHandle(h)
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False
    except Exception:
        # En CPython un pid inexistente puede lanzar SystemError; se trata como muerto.
        return False


@contextlib.contextmanager
def bloqueo(ruta: Path, vencimiento: float = 180.0) -> Iterator[bool]:
    """Bloqueo entre procesos. Cede True si se obtuvo, False si ya estaba tomado.

    Nunca lanza. Respeta el vencimiento y la propiedad: si el duenno sigue vivo,
    el lock no se roba aunque su mtime sea viejo.
    """
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    obtenido = False
    for _ in range(2):
        try:
            fd = os.open(str(ruta), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()} {time.time()}".encode("ascii"))
            os.close(fd)
            obtenido = True
            break
        except FileExistsError:
            try:
                pid = int(ruta.read_text(encoding="ascii").split()[0])
            except (OSError, ValueError, IndexError):
                pid = -1
            if pid == os.getpid():
                break
            if edad_segundos(ruta) < vencimiento or proceso_vivo(pid):
                break
            with contextlib.suppress(OSError):
                ruta.unlink()
    try:
        yield obtenido
    finally:
        if obtenido:
            with contextlib.suppress(OSError):
                ruta.unlink()
