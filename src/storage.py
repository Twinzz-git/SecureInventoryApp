import json
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil

def load_json(path: Path, default):
    """Carga un archivo JSON o devuelve un valor por defecto si no existe o está corrupto."""
    if not path.exists():
        # Si no existe, lo crea con el contenido por defecto
        path.write_text(json.dumps(default, ensure_ascii=False, indent=2), encoding='utf-8')
        return default
    try:
        text = path.read_text(encoding='utf-8')
        return json.loads(text)
    except Exception:
        # Si el archivo está dañado o tiene errores de formato
        return default

def save_json_atomic(path: Path, data):
    """Guarda datos JSON de forma segura (escribe en un archivo temporal y luego reemplaza el original)."""
    dirpath = path.parent
    dirpath.mkdir(parents=True, exist_ok=True)  # crea la carpeta si no existe
    with NamedTemporaryFile('w', delete=False, dir=dirpath, encoding='utf-8') as tf:
        json.dump(data, tf, ensure_ascii=False, indent=2)
        tmpname = tf.name
    shutil.move(tmpname, str(path))
