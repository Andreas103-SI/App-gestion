import psutil

def get_system_usage():
    # Obtiene el uso de la CPU (porcentaje durante 1 segundo)
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Obtiene el uso de la memoria (porcentaje)
    memory_usage = psutil.virtual_memory().percent
    
    # Obtiene el uso de almacenamiento (porcentaje)
    # Nota: En Windows, si quieres obtener la información del disco principal, podrías usar 'C:\\'
    disk_usage = psutil.disk_usage('C:\\').percent

    return {
        'cpu': cpu_usage,
        'memory': memory_usage,
        'disk': disk_usage
    }

if __name__ == '__main__':
    usage = get_system_usage()
    print(f"Uso de CPU: {usage['cpu']}%")
    print(f"Uso de Memoria: {usage['memory']}%")
    print(f"Uso de Disco: {usage['disk']}%")
