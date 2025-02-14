# config.py
import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Ajusta según tu configuración
    MYSQL_DB = 'proyecto_app'
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones

    # Configuración de caché
    CACHE_TYPE = 'simple'  # Usa caché en memoria
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutos de tiempo de expiración
