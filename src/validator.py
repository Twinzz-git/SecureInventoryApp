import re

def validar_username(username: str) -> bool:
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True


def validar_email(email: str) -> bool:
    # patrón básico de correo electrónico
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, email):
        return False
    return True


def validar_password(password: str) -> bool:
    # revisa longitud mínima, al menos una letra y un número
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True
