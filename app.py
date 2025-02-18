
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify
from monitor import get_system_usage
from optimizer import check_processes, optimize_processes
from send import send_notification
from reports import get_system_report
from logger_config import logger
import csv
from flask import Response
from reportlab.pdfgen import canvas
from io import BytesIO, StringIO
import cProfile
import pstats
from flask_caching import Cache
from config import Config



app = Flask(__name__)
app.config.from_object('config.Config')  # Cargar configuración desde config.py

app.config['CACHE_TYPE'] = 'simple'  # Usando caché simple en memoria
cache = Cache(app, config={

}) # Inicializar la extensión de cach

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Tu contraseña de MySQL si tienes una
app.config['MYSQL_DB'] = 'proyecto_app'

mysql = MySQL(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



# Modelo de usuario
class User(UserMixin):
    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol


# Cargar el usuario por ID
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    data = cursor.fetchone()
    if data:
        return User(id=data[0], nombre=data[1], email=data[2], rol=data[4])
    return None


# Ruta de la página de inicio
@app.route('/')
@login_required
def index():
    return render_template('index.html')


# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            user_data = cursor.fetchone()
            if user_data and check_password_hash(user_data[3], password):
                user = User(id=user_data[0], nombre=user_data[1], email=user_data[2], rol=user_data[4])
                login_user(user)
                logger.info(f"El usuario {email} inició sesión correctamente.")
                return redirect(url_for('index'))
            else:
                logger.warning(f"Intento fallido de inicio de sesión para el email: {email}")
                return "Credenciales incorrectas, inténtalo nuevamente."
        except Exception as e:
            logger.exception("Error durante el proceso de login")
            return "Ha ocurrido un error en el proceso de login", 500
    return render_template('login.html')


# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# Ruta para gestionar usuarios

@app.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuarios():
    # Verificar si el usuario actual es administrador
    if current_user.rol != 'admin':
        return "Acceso no autorizado. Solo los administradores pueden acceder a esta página.", 403

    cursor = mysql.connection.cursor()
    # Obtener todos los usuarios
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    if request.method == 'POST':
        user_id = request.form.get('id')
        action = request.form.get('action')
        
        if action == 'edit':
            nombre = request.form['nombre']
            email = request.form['email']
            cursor.execute("UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s", (nombre, email, user_id))
            mysql.connection.commit()
        elif action == 'delete':
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
            mysql.connection.commit()

        return redirect(url_for('usuarios'))

    return render_template('usuarios.html', usuarios=usuarios)


# Ruta para registrar un nuevo usuario
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        try:
            password_hash = generate_password_hash(password)
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, email, password) 
                              VALUES (%s, %s, %s)''', (nombre, email, password_hash))
            mysql.connection.commit()
            cursor.close()
            logger.info(f"Usuario registrado: {email}")
            return redirect(url_for('login'))
        except Exception as e:
            logger.exception("Error durante el registro de usuario")
            return "Error en el registro del usuario", 500
    return render_template('registrar.html')


# Ruta para monitorear el sistema
@app.route('/monitor')
def monitor():
    # Llama a la función 'get_system_usage()' que obtiene el uso de CPU, memoria y disco.
    usage = get_system_usage()
    
    # Devuelve la información obtenida en formato JSON, lo que facilita su uso en aplicaciones web o APIs.
    return jsonify(usage)

@app.route('/monitor_view')
def monitor_view():
    # Esta ruta renderiza la plantilla HTML 'monitor.html', mostrando la información de monitoreo.
    return render_template('monitor.html')


#Rura de optimizacion de procesos
@app.route('/optimizer')
def optimizer():
    try:
        inefficient_processes = check_processes()
        if inefficient_processes:
            optimize_processes(inefficient_processes)
            send_notification(mysql, inefficient_processes)
            logger.info("Procesos ineficientes detectados y optimizados.")
            return jsonify({
                'status': 'success',
                'message': 'Procesos ineficientes terminados y administrador notificado.',
                'inefficient_processes': inefficient_processes
            }), 200
        else:
            logger.info("No se encontraron procesos ineficientes.")
            return jsonify({
                'status': 'success',
                'message': 'No se encontraron procesos ineficientes.'
            }), 200
    except Exception as e:
        logger.exception("Error durante la optimización de procesos")
        return jsonify({'status': 'error', 'message': 'Error en la optimización.'}), 500


#Gestion de tareas Administrativas
''' Aqui se muestra la gestion de tareas administrativas, como la creacion de notificaciones de limpieza de logs'''


@app.route('/notificaciones')
@login_required
def notificaciones():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM notificaciones ORDER BY fecha DESC")
    notificaciones = cursor.fetchall()
    return render_template('notificaciones.html', notificaciones=notificaciones)

# Ruta para mostrar el informe del sistema en una plantilla HTML
@app.route('/system_report')
def system_report():
    report = get_system_report()  # Obtiene el informe desde 'reports.py'
    return render_template('system_report.html', report=report)

# Ruta para exportar el informe a CSV
@app.route('/export_csv')
def export_csv():
    report = get_system_report()  # Obtiene el informe del sistema

    # Prepara los datos del informe
    output = []
    output.append(['Fecha y Hora', report['timestamp']])
    output.append(['Procesos Activos', report['active_processes']])
    output.append(['Uso de CPU (%)', report['cpu_usage']])
    output.append(['Uso de Disco (%)', report['disk_usage']])
    output.append(['Uso de Memoria (%)', report['memory_usage']])
    
    si = BytesIO()  # Usamos BytesIO para trabajar con datos binarios
    writer = csv.writer(si)
    writer.writerows(output)
    si.seek(0)

    return Response(si.getvalue(),
                    mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=system_report.csv"})

# Ruta para exportar el informe a PDF
@app.route('/export_pdf')
def export_pdf():
    report = get_system_report()  # Obtiene el informe del sistema
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Título del informe
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 800, "Informe de Uso del Sistema")
    
    # Contenido del informe
    pdf.setFont("Helvetica", 12)
    y = 770
    pdf.drawString(50, y, f"Fecha y Hora: {report['timestamp']}")
    y -= 20
    pdf.drawString(50, y, f"Procesos Activos: {report['active_processes']}")
    y -= 20
    pdf.drawString(50, y, f"Uso de CPU (%): {report['cpu_usage']}")
    y -= 20
    pdf.drawString(50, y, f"Uso de Disco (%): {report['disk_usage']}")
    y -= 20
    pdf.drawString(50, y, f"Uso de Memoria (%): {report['memory_usage']}")
    
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return Response(buffer.getvalue(),
                    mimetype="application/pdf",
                    headers={"Content-Disposition": "attachment; filename=system_report.pdf"})


#Ruta para la gestion de tareas administrativas
@app.route('/data')
def data():
    return 'Datos importantes'

def profile_view():
    profiler = cProfile.Profile()
    profiler.enable()

    # Llama a la ruta que quieres perfilar
    with app.test_client() as client:
        response = client.get('/data')  # Simula una solicitud GET a la ruta /data

    profiler.disable()

    # Guardar el perfil de estadísticas en un archivo
    profiler.dump_stats('profile_stats.prof')

    # Cargar el archivo de estadísticas
    stats = pstats.Stats('profile_stats.prof')

    # Imprimir los datos de profiling en la consola
    stats.sort_stats('cumulative').print_stats(5)  # Muestra las 5 funciones más lentas

    return response.data



# Ruta de prueba para caché
@app.route('/test_cache')
@cache.cached(timeout=60)  # Se almacena en caché por 60 segundos
def test_cache():
    import time
    time.sleep(5)  # Simula una operación lenta
    return "Esta respuesta fue almacenada en caché."


if __name__ == '__main__':
    print("🚀 Servidor corriendo en http://127.0.0.1:5000")
    print("🔍 Monitoreo de recursos: http://127.0.0.1:5000/monitor_view")
    print("⚡ Optimización de procesos: http://127.0.0.1:5000/optimizer")

    profile_view()  # Llama a la función que ejecuta el perfilado
    app.run(debug=True)
