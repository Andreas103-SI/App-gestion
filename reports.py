import psutil
import datetime

def get_system_report():
    """Obtiene datos del rendimiento del sistema."""
    report = {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'active_processes': len(psutil.pids())
    }
    return report
