import psutil


def check_processes():
    """Obtiene los procesos ineficientes (por ejemplo, uso alto de CPU o memoria)."""
    inefficient_processes = []
    # Aquí puedes definir el criterio para identificar procesos ineficientes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        if proc.info['cpu_percent'] > 80 or proc.info['memory_percent'] > 80:
            inefficient_processes.append(proc.info)
    return inefficient_processes

def optimize_processes(processes):
    """Termina los procesos ineficientes."""
    for process in processes:
        try:
            psutil.Process(process['pid']).terminate()  # Intenta terminar el proceso.
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        

# Activar este código solo si tienes configurado un servidor SMTP para enviar correos electrónicos.
''' Tarea pendiente para cuando cree la gestion de rolles y usuarios
def send_notification(inefficient_processes, admin_email='andreasierra1223@gmail.com'):
    """
    Envía un correo electrónico notificando al administrador sobre los procesos ineficientes.
    """
    if not inefficient_processes:
        return

    message_body = "Se han detectado procesos ineficientes:\n\n"
    for proc in inefficient_processes:
        message_body += (
            f"Proceso: {proc['name']} (PID: {proc['pid']}) - "
            f"CPU: {proc['cpu']}% - Memoria: {proc['memory']}%\n"
        )

    msg = MIMEText(message_body)
    msg['Subject'] = 'Alerta: Procesos ineficientes detectados'
    msg['From'] = 'andreasierra1223@gmail.com'
    msg['To'] = admin_email

    try:
        # Configura tu servidor SMTP según tu proveedor
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_user = 'andreasierra1223@gmail.com'
        smtp_password = 'tu-contraseña'
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(msg['From'], [admin_email], msg.as_string())
        server.quit()
        print("Notificación enviada al administrador.")
    except Exception as e:
        print("Error al enviar la notificación:", e)'''
