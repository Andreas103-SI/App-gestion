
def send_notification(mysql, inefficient_processes):
    """
    Inserta una notificación en la base de datos para informar al administrador
    de que se han terminado procesos ineficientes.
    """
    # Crea el mensaje a partir de los procesos ineficientes
    message = 'Procesos ineficientes terminados: ' + str(inefficient_processes)
    
    # Abre un cursor para insertar la notificación
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO notificaciones (tarea, mensaje, estado) VALUES (%s, %s, %s)",
        ('Optimizer', message, 'exito')
    )
    mysql.connection.commit()
    cursor.close()
