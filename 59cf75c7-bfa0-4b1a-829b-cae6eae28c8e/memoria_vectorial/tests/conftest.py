import os
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

_BOVEDA = Path(tempfile.mkdtemp(prefix="memoria_test_"))
os.environ["MEMORIA_BOVEDA"] = str(_BOVEDA)
os.environ["MEMORIA_MIN_SIM"] = "0.35"

for sub in ("Sistema", "Perfil", "LLM-Memoria/Hechos", "LLM-Memoria/Web",
            "Diario", "skills", "_descartados", ".memoria"):
    (_BOVEDA / sub).mkdir(parents=True, exist_ok=True)
