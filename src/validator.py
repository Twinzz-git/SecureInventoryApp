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

def validar_sku(sku: str) -> bool:
    # SKU debe ser alfanumérico y tener entre 5 y 10 caracteres
    if len(sku) < 5 or len(sku) > 10:
        return False
    if not sku.isalnum():
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


