# src/logger.py
from pathlib import Path
from datetime import datetime

logfile = Path("logs/log.txt")


def log_action(username: str, action: str):
    """Registra una acción en el archivo de log."""
    # Crear carpeta logs si no existe
    logfile.parent.mkdir(parents=True, exist_ok=True)
    
    # Obtener fecha y hora actual
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear línea de log
    log_entry = f"[{timestamp}] User: {username} - Action: {action}\n"
    
    # Escribir en el archivo
    archivo = open(logfile, "a", encoding="utf-8")
    archivo.write(log_entry)
    archivo.close()