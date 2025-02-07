# config.py
import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Ajusta según tu configuración
    MYSQL_DB = 'proyecto_app'
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones
