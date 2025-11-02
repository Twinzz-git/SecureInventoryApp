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

def validarproductname(name: str) -> bool:
    # Nombre debe tener entre 2 y 50 caracteres
    if len(name) < 2 or len(name) > 50:
        return False
    # Permitir letras, números, espacios y algunos símbolos
    if not re.match(r'^[a-zA-Z0-9\s\-\_\.]+$', name):
        return False
    return True

def validar_price(price: float) -> bool:
    # El precio debe ser un número positivo
    if price <= 0:
        return False
    return True

def validar_stock(stock: int) -> bool:
    
    if stock < 0:
        return False
    return True


