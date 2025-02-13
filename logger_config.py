import os
import logging
from logging.handlers import TimedRotatingFileHandler

# Crear el directorio de logs si no existe
log_dir = os.path.join(os.getcwd(), "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuración del logger
logger = logging.getLogger("mi_app_logger")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(os.path.join(log_dir, "app_log.log"), when="h", interval=2, backupCount=10)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
