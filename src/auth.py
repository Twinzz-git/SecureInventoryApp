# src/auth.py
import json
import hashlib
from pathlib import Path

# Archivo donde se guardarán los usuarios
Userfile = Path("data/users.json")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# 📝 Registrar usuario
def register_user(username: str, email: str, password: str, role: str = "user") -> bool:
    try:
        # Cargar usuarios existentes
        if Userfile.exists():
            users = json.loads(Userfile.read_text(encoding="utf-8"))
        else:
            users = []

        # Evitar duplicados
        for u in users:
            if u['username'] == username or u['email'] == email:
                return False  # usuario ya existe

        # Agregar nuevo usuario
        users.append({
            "username": username,
            "email": email,
            "password_hash": hash_password(password),
            "role": role
        })

        # Guardar de nuevo en el archivo
        Userfile.parent.mkdir(parents=True, exist_ok=True)
        Userfile.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    
    except Exception:
        return False


def login_user(email: str, password: str):
    try:
        if not Userfile.exists():
            return None  # no hay usuarios

        users = json.loads(Userfile.read_text(encoding="utf-8"))

        for u in users:
            if u['email'] == email and u['password_hash'] == hash_password(password):
                return u  # login exitoso, devuelve diccionario del usuario

        return None  # login fallido
    
    except Exception:
        return None