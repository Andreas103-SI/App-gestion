from flask import Flask, jsonify  # Importamos Flask y jsonify para manejar la API y respuestas JSON
import psutil  # Librería para obtener métricas del sistema

app = Flask(__name__)  # Creamos la aplicación Flask

@app.route('/api/recursos', methods=['GET'])  # Definimos una ruta para obtener las métricas
def obtener_recursos():
    # Obtenemos datos del sistema con psutil
    datos = {
        "cpu": psutil.cpu_percent(interval=1),  # Uso de CPU en porcentaje
        "memoria_total": round(psutil.virtual_memory().total / (1024**3), 2),  # Memoria total en GB
        "memoria_usada": round(psutil.virtual_memory().used / (1024**3), 2),  # Memoria usada en GB
        "memoria_porcentaje": psutil.virtual_memory().percent,  # Uso de memoria en porcentaje
        "almacenamiento_total": round(psutil.disk_usage('/').total / (1024**3), 2),  # Almacenamiento total en GB
        "almacenamiento_usado": round(psutil.disk_usage('/').used / (1024**3), 2),  # Almacenamiento usado en GB
        "almacenamiento_porcentaje": psutil.disk_usage('/').percent  # Uso de almacenamiento en porcentaje
    }
    return jsonify(datos)  # Convertimos los datos a JSON y los enviamos como respuesta

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Iniciamos la API en el puerto 5001
