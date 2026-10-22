"""
Crea skills (borradores) a partir de lo que ya aprendió, dirigido por código.

Para cada skill, el script (no el LLM):
  1. Le muestra al LLM los títulos/etiquetas de las notas aprendidas y le pide candidatos
     (nombre | descripción | palabras clave).
  2. Busca en la memoria (notas y fragmentos de tus archivos) lo relacionado con cada candidato.
  3. Le pide al LLM SOLO el cuerpo de la skill; el encabezado (name, description) y la lista de
     fuentes los escribe el código.
  4. Guarda skills\\<nombre>\\SKILL.md. Si esa carpeta ya existe, la salta: nunca sobrescribe.

Uso:
  python crear_skills.py                  hasta 8 skills nuevas (reanudable)
  python crear_skills.py --max 3          solo 3 (para probar)
  python crear_skills.py --status
Variables: SKILLS_DIR (por defecto <bóveda>\\skills), LLM_MODEL.
Las skills son BORRADORES hechos por un modelo pequeño con tus notas: revísalas antes de confiar.
"""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import aprender
import memoria

VAULT = memoria.VAULT
SKILLS_DIR = Path(os.environ.get("SKILLS_DIR", str(VAULT / "skills")))
MEM_DIR = aprender.MEM_DIR
STATE_PATH = VAULT / ".memoria" / "skills.json"
STOP_PATH = aprender.STOP_PATH
MAX_NOTAS_LISTA = 120
MAX_CONTEXTO = 9000
CANDIDATOS_POR_RONDA = 5

SISTEMA_CANDIDATOS = (
    "Eres un organizador de conocimiento que propones skills. Una skill es una guía reutilizable y concreta "
    "para una tarea o un tipo de proyecto que se repite (por ejemplo: cómo armar una landing de cierto estilo, "
    "cómo estructurar un workflow, cómo configurar una herramienta). Recibes la lista de lo que ya se aprendió. "
    "Responde SOLO con líneas en este formato exacto, sin numeración ni explicaciones:\n"
    "nombre-en-kebab-case | descripción de una frase (qué hace y cuándo usarla) | 3 a 6 palabras clave para buscar"
)
SISTEMA_SKILL = (
    "Redactas skills claras y prácticas en español. Recibes el material (notas y fragmentos de archivos reales) y "
    "escribes SOLO el cuerpo de la skill, con estas secciones exactas:\n"
    "# <Título>\n## Propósito\n## Cuándo usarla\n## Pasos\n## Reglas\n## Errores comunes\n\n"
    "Reglas: usa únicamente lo que dice el material; si algo falta escribe 'pendiente de confirmar' en vez de inventar; "
    "los pasos son numerados y concretos; puedes incluir fragmentos de código cortos tomados del material; "
    "máximo 450 palabras; nunca incluyas contraseñas, claves ni tokens; responde solo con el cuerpo, sin saludos."
)


# --------------------------------------------------------------------------
def kebab(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower().strip().replace("_", "-"))
    return s.strip("-")[:50]


def cargar():
    try:
        e = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        e = {}
    e.setdefault("hechas", {})
    e.setdefault("saltadas", {})
    return e


def guardar(e):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, STATE_PATH)


def leer_notas():
    """[{'titulo','fuente','tags','resumen','ruta'}] de las notas de Hechos."""
    notas = []
    if not aprender.HECHOS.is_dir():
        return notas
    for p in sorted(aprender.HECHOS.rglob("*.md")):
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "etapa: aprendizaje" not in t:
            continue
        fuente = (re.search(r'^fuente:\s*"?(.*?)"?\s*$', t, re.M) or [None, ""])[1]
        titulo = (re.search(r"^# (.+)$", t, re.M) or [None, p.stem])[1]
        resumen = (re.search(r"## Resumen\s+(.*?)(?=\n## |\Z)", t, re.S) or [None, ""])[1].strip()
        tags = (re.search(r"## Etiquetas\s+(.*?)(?=\n## |\Z)", t, re.S) or [None, ""])[1].strip()
        notas.append({"titulo": titulo, "fuente": fuente, "tags": tags, "resumen": resumen,
                      "ruta": p.relative_to(VAULT).as_posix()})
    return notas


def lista_para_modelo(notas):
    if len(notas) > MAX_NOTAS_LISTA:
        paso = len(notas) / MAX_NOTAS_LISTA
        notas = [notas[int(i * paso)] for i in range(MAX_NOTAS_LISTA)]
    out = []
    for n in notas:
        carpeta = "/".join(n["fuente"].split("/")[:-1][-2:])
        out.append(f"- {carpeta} :: {n['titulo']} :: {n['tags'][:80]}")
    return "\n".join(out)


def skills_existentes():
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(d.name for d in SKILLS_DIR.iterdir() if d.is_dir())


def ejemplos_de_formato():
    """Hasta 2 skills ya existentes, para que el modelo copie su estilo."""
    out = []
    for nombre in skills_existentes():
        f = SKILLS_DIR / nombre / "SKILL.md"
        if f.is_file():
            try:
                out.append(f.read_text(encoding="utf-8", errors="replace")[:1500])
            except OSError:
                pass
        if len(out) >= 2:
            break
    return out


def pedir_candidatos(modelo, notas, ya):
    usuario = (
        "Lo aprendido (carpeta :: archivo :: etiquetas):\n" + lista_para_modelo(notas) +
        f"\n\nPropón hasta {CANDIDATOS_POR_RONDA} skills útiles y distintas entre sí.\n"
        "No repitas ni se parezcan a estas (ya existen o ya se intentaron): " + (", ".join(sorted(ya)) or "(ninguna)")
    )
    txt = aprender.memoria._http("POST", "/chat/completions", {
        "model": modelo,
        "messages": [{"role": "system", "content": SISTEMA_CANDIDATOS}, {"role": "user", "content": usuario}],
        "temperature": 0.4, "max_tokens": 600,
        "chat_template_kwargs": {"enable_thinking": False},
    }, timeout=900)["choices"][0]["message"].get("content") or ""
    txt = re.sub(r"<think>.*?</think>", "", txt, flags=re.S).split("<think>")[0]
    candidatos = []
    for linea in txt.splitlines():
        partes = [p.strip(" -*`") for p in linea.split("|")]
        if len(partes) >= 3 and partes[0]:
            nombre = kebab(partes[0])
            if len(nombre) >= 3 and nombre not in ya and nombre not in [c[0] for c in candidatos]:
                candidatos.append((nombre, partes[1][:200], partes[2][:120]))
    return candidatos[:CANDIDATOS_POR_RONDA]


def reunir_material(notas, palabras):
    """Notas relacionadas (por palabras clave) + fragmentos de la memoria. Devuelve (texto, fuentes)."""
    claves = {w for w in re.findall(r"\w+", palabras.lower()) if len(w) > 2}
    puntuadas = []
    for n in notas:
        base = (n["titulo"] + " " + n["tags"] + " " + n["resumen"]).lower()
        s = sum(1 for w in claves if w in base)
        if s:
            puntuadas.append((s, n))
    puntuadas.sort(key=lambda x: -x[0])
    partes, fuentes, total = [], [], 0
    for _, n in puntuadas[:4]:
        bloque = f"[Nota: {n['fuente']}]\n{n['resumen'][:800]}\n{n['tags']}"
        partes.append(bloque)
        fuentes.append(n["fuente"] or n["ruta"])
        total += len(bloque)
    try:
        resultados, _ = memoria.search(palabras, 6, auto_sync=False, ambito="mios")
        for r in resultados:
            if r["ruta"].startswith(aprender.MEM_DIR.name + "/Hechos"):
                continue  # las notas ya se incluyeron arriba
            if r["ruta"].startswith(SKILLS_DIR.name + "/"):
                continue  # las skills no se alimentan de otras skills generadas (acumularían errores)
            bloque = f"[Archivo: {r['ruta']}]\n{r['texto'][:1200]}"
            if total + len(bloque) > MAX_CONTEXTO:
                break
            partes.append(bloque)
            fuentes.append(r["ruta"])
            total += len(bloque)
    except (memoria.EmbeddingError, Exception):  # noqa: BLE001  - sin índice: se sigue solo con las notas
        pass
    return "\n\n".join(partes), list(dict.fromkeys(fuentes))


def pedir_cuerpo(modelo, nombre, descripcion, material, ejemplos):
    usuario = f"Skill: {nombre}\nDescripción: {descripcion}\n\n"
    if ejemplos:
        usuario += "Ejemplos del formato de skills que ya existen:\n" + "\n---\n".join(ejemplos) + "\n\n"
    usuario += "Material (úsalo como única fuente):\n<<<\n" + material[:MAX_CONTEXTO] + "\n>>>"
    txt = memoria._http("POST", "/chat/completions", {
        "model": modelo,
        "messages": [{"role": "system", "content": SISTEMA_SKILL}, {"role": "user", "content": usuario}],
        "temperature": 0.3, "max_tokens": 2000,
        "chat_template_kwargs": {"enable_thinking": False},
    }, timeout=900)["choices"][0]["message"].get("content") or ""
    txt = re.sub(r"<think>.*?</think>", "", txt, flags=re.S).split("<think>")[0].strip()
    txt = re.sub(r"^```(?:markdown|md)?\s*|\s*```$", "", txt).strip()
    if txt.startswith("---"):  # el modelo repitió un encabezado: se descarta, lo escribe el código
        partes = txt.split("---", 2)
        txt = partes[2].strip() if len(partes) == 3 else txt
    if len(txt) < 200 or "## Pasos" not in txt:
        raise ValueError("cuerpo incompleto (faltan secciones o es muy corto)")
    return txt


def escribir_skill(nombre, descripcion, cuerpo, fuentes):
    d = SKILLS_DIR / nombre
    d.mkdir(parents=True, exist_ok=False)  # falla si ya existe: nunca se sobrescribe
    contenido = (
        "---\n"
        f"name: {nombre}\n"
        f"description: {descripcion}\n"
        "---\n\n"
        "> Borrador generado automáticamente a partir de lo aprendido. Revisar antes de confiar.\n\n"
        f"{cuerpo}\n\n"
        "## Fuentes\n" + "\n".join(f"- {f}" for f in fuentes) + "\n"
    )
    (d / "SKILL.md").write_text(contenido, encoding="utf-8")
    return (d / "SKILL.md")


def registrar(nombre, descripcion, fuentes):
    try:
        carpeta = MEM_DIR / "Decisiones"
        carpeta.mkdir(parents=True, exist_ok=True)
        f = carpeta / f"skills-{datetime.now():%Y-%m-%d}.md"
        if not f.exists():
            f.write_text(f"---\nfecha: {datetime.now():%Y-%m-%d}\netapa: skills\ntags: [skills]\n---\n# Skills creadas\n", encoding="utf-8")
        with f.open("a", encoding="utf-8") as fh:
            fh.write(f"\n- {datetime.now():%H:%M} `{nombre}`: {descripcion} (fuentes: {', '.join(fuentes[:4])})\n")
    except OSError:
        pass


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Crea skills a partir de lo aprendido")
    ap.add_argument("--max", type=int, default=8, help="skills nuevas como máximo en esta ejecución")
    ap.add_argument("--model", help="modelo de chat de LM Studio")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    estado = cargar()
    if args.status:
        print(f"Skills creadas: {len(estado['hechas'])} | candidatas saltadas: {len(estado['saltadas'])} | "
              f"carpetas en {SKILLS_DIR}: {len(skills_existentes())}")
        return 0

    notas = leer_notas()
    if not notas:
        print("Todavía no hay notas aprendidas en LLM-Memoria\\Hechos: nada que convertir en skills.")
        return 0
    try:
        modelo = aprender.modelo_chat(args.model)
    except memoria.EmbeddingError as e:
        print("Error:", e, file=sys.stderr)
        return 2
    print(f"Notas disponibles: {len(notas)} | Modelo: {modelo} | Skills en: {SKILLS_DIR}")

    creadas, rondas_vacias, sin_conexion = 0, 0, 0
    try:
        while creadas < args.max and rondas_vacias < 2 and not STOP_PATH.exists():
            ya = set(skills_existentes()) | set(estado["hechas"]) | set(estado["saltadas"])
            try:
                candidatos = pedir_candidatos(modelo, notas, ya)
            except memoria.ConexionError:
                if sin_conexion >= aprender.MAX_SIN_CONEXION:
                    print("LM Studio lleva 30 min sin responder: me detengo.")
                    return 2
                print("LM Studio no responde; reintento en 60 s...")
                time.sleep(aprender.ESPERA_CONEXION)
                sin_conexion += aprender.ESPERA_CONEXION
                continue
            except (memoria.EmbeddingError, KeyError, IndexError) as e:
                print("No pude obtener candidatos:", str(e)[:100])
                rondas_vacias += 1
                continue
            sin_conexion = 0
            if not candidatos:
                rondas_vacias += 1
                print("Sin candidatos nuevos en esta ronda.")
                continue

            nuevas_en_ronda = 0
            for nombre, descripcion, palabras in candidatos:
                if creadas >= args.max or STOP_PATH.exists():
                    break
                if (SKILLS_DIR / nombre).exists():
                    estado["saltadas"][nombre] = "ya existe"
                    print(f"- {nombre}: ya existe, se salta")
                    continue
                material, fuentes = reunir_material(notas, f"{nombre.replace('-', ' ')} {palabras}")
                if len(material) < 200:
                    estado["saltadas"][nombre] = "sin material suficiente"
                    print(f"- {nombre}: sin material suficiente, se salta")
                    continue
                cuerpo, intentos = None, 0
                while cuerpo is None and intentos < 3:
                    intentos += 1
                    try:
                        cuerpo = pedir_cuerpo(modelo, nombre, descripcion, material, ejemplos_de_formato())
                    except memoria.ConexionError:
                        print("  LM Studio no responde; espero 60 s...")
                        time.sleep(aprender.ESPERA_CONEXION)
                        intentos -= 1
                        sin_conexion += aprender.ESPERA_CONEXION
                        if sin_conexion >= aprender.MAX_SIN_CONEXION:
                            print("LM Studio lleva 30 min sin responder: me detengo.")
                            return 2
                    except (memoria.EmbeddingError, ValueError, KeyError, IndexError) as e:
                        print(f"  {nombre}: intento {intentos}/3 falló: {str(e)[:80]}")
                if cuerpo is None:
                    estado["saltadas"][nombre] = "falló 3 veces"
                    guardar(estado)
                    continue
                try:
                    escribir_skill(nombre, descripcion, cuerpo, fuentes)
                except OSError as e:
                    estado["saltadas"][nombre] = f"no se pudo escribir: {e}"
                    guardar(estado)
                    continue
                estado["hechas"][nombre] = {"fecha": f"{datetime.now():%F}", "fuentes": fuentes[:6]}
                registrar(nombre, descripcion, fuentes)
                guardar(estado)
                creadas += 1
                nuevas_en_ronda += 1
                print(f"- {nombre}: creada ({creadas}/{args.max})")
                try:
                    memoria.indexar_archivo((SKILLS_DIR / nombre / "SKILL.md").relative_to(VAULT).as_posix())
                except Exception:  # noqa: BLE001
                    pass
            rondas_vacias = 0 if nuevas_en_ronda else rondas_vacias + 1
            guardar(estado)
    except KeyboardInterrupt:
        print("\nInterrumpido: el avance ya está guardado.")
    finally:
        guardar(estado)
    print(f"Fin. Skills nuevas en esta ejecución: {creadas}. Revísalas en {SKILLS_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
