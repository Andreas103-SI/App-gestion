# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify
from monitor import get_system_usage
from optimizer import check_processes, optimize_processes

app = Flask(__name__)
app.config.from_object('config.Config')

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
        # Obtener los datos del formulario
        email = request.form['email']
        password = request.form['password']
        
        # Guardar los datos en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user_data = cursor.fetchone()

        if user_data and check_password_hash(user_data[3], password):  # Compara con el hash de la contraseña
            user = User(id=user_data[0], nombre=user_data[1], email=user_data[2], rol=user_data[4])
            login_user(user)
            return redirect(url_for('index'))
        else:
            return "Credenciales incorrectas, inténtalo nuevamente."

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
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        # Hashear la contraseña antes de almacenarla
        password = generate_password_hash(password)

        # Guardar los datos en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO usuarios (nombre, email, password) 
                          VALUES (%s, %s, %s)''', (nombre, email, password))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('login'))  # Redirigir a la página de login
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

@app.route('/optimizer')
def optimizer():
    # Llama a la función que obtiene los procesos ineficientes (por CPU o memoria alta).
    inefficient_processes = check_processes()

    # Si hay procesos ineficientes, los optimizamos (terminamos).
    if inefficient_processes:
        optimize_processes(inefficient_processes)
        # Enviar la notificación al administrador si es necesario (aunque aquí está comentado).
        '''send_notification(inefficient_processes)'''

        # Respuesta indicando que los procesos fueron terminados y notificados.
        return jsonify({
            'status': 'success',
            'message': 'Procesos ineficientes terminados y administrador notificado.',
            'inefficient_processes': inefficient_processes
        }), 200
    else:
        # Si no hay procesos ineficientes, devolvemos un mensaje indicando que todo está bien.
        return jsonify({
            'status': 'success',
            'message': 'No se encontraron procesos ineficientes.'
        }), 200

#Gestion de tareas Administrativas
''' Aqui se muestra la gestion de tareas administrativas, como la creacion de notificaciones de limpieza de logs'''


@app.route('/notificaciones')
@login_required
def notificaciones():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM notificaciones ORDER BY fecha DESC")
    notificaciones = cursor.fetchall()
    return render_template('notificaciones.html', notificaciones=notificaciones)


if __name__ == '__main__':
    print("🚀 Servidor corriendo en http://127.0.0.1:5000")
    print("🔍 Monitoreo de recursos: http://127.0.0.1:5000/monitor_view")
    print("⚡ Optimización de procesos: http://127.0.0.1:5000/optimizer")
    app.run(debug=True)
