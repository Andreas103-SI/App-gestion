# Proyecto App - Gestión Administrativa y Optimización de Recursos

## Descripción

Esta aplicación web está desarrollada utilizando Python y Flask. Su objetivo es facilitar la gestión administrativa y la optimización de recursos en sistemas informáticos. La aplicación incluye funcionalidades para la gestión de usuarios, autenticación, monitoreo de recursos, optimización de procesos, generación de informes detallados y pruebas automatizadas para asegurar la calidad del código.

## Funcionalidades

### 1. Gestión de Usuarios
- Visualización de todos los usuarios registrados.
- Edición y eliminación de usuarios (solo accesible para administradores).
- Gestión de usuarios mediante una interfaz intuitiva con botones.

### 2. Autenticación de Usuarios
- Inicio de sesión con correo electrónico y contraseña.
- Registro de nuevos usuarios con validación de datos.
- Recuperación de contraseña (si se implementa).

### 3. Monitoreo de Recursos del Sistema
- Visualización en tiempo real del uso de CPU, memoria y disco.
- Interfaz gráfica accesible desde la aplicación.
- Endpoint para obtener datos en formato JSON: `http://127.0.0.1:5000/monitor`.

### 4. Optimización de Procesos
- Detección de procesos ineficientes basados en el uso de CPU y memoria.
- Optimización automática de procesos problemáticos.
- Notificaciones al administrador en caso de sobrecarga de recursos (configurable).
- Endpoint para optimización: `http://127.0.0.1:5000/optimizer`.

### 5. Generación y Exportación de Informes
- Informe detallado sobre el rendimiento del sistema (incluye tiempos de respuesta y utilización de recursos).
- Visualización de informes en una página dedicada.
- Exportación de informes en formatos CSV y PDF mediante botones en la interfaz.

### 6. Pruebas Automatizadas
- **Objetivo:** Garantizar la estabilidad y calidad del código.
- **Herramientas:** Se pueden utilizar frameworks como `pytest` o `unittest`.

## Requisitos
- Python 3.x
- MySQL (se puede gestionar con XAMPP)
- Flask
- Dependencias adicionales (ver requirements.txt)

## Instalación
** clonar repositorio**
git clone https://github.com/Andreas103-SI/ProyectoApp.git
cd proyecto_app

2. Crear un entorno virtual e instalar dependencias

python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

3. Instalar dependencias adicionales
pip install flask-caching
pip install pytest

4. Configurar la base de datos
Asegúrate de que MySQL esté corriendo (por ejemplo, con XAMPP) y crea la base de datos:

Configura las credenciales de la base de datos en el archivo config.py.

5. Ejecutar la aplicación

python app.py

- La aplicación estará disponible en http://127.0.0.1:5000/.

6. Ejecutar los test 

venv\Scripts\python.exe -m pytest


### Notas
- El archivo .gitignore está configurado para excluir archivos innecesarios, como __pycache__ y el entorno virtual venv.
- Se recomienda actualizar pip a la última versión:
  python -m pip install --upgrade pip
- Algunas funcionalidades, como el envío de notificaciones por correo electrónico, requieren       configuración adicional.
- La aplicación utiliza herencia de plantillas con Jinja2 para mantener una interfaz consistente en todas las páginas.
- Las pruebas automatizadas ayudan a garantizar que las futuras optimizaciones y cambios no introduzcan errores en la aplicación.

### Contribución 
Si deseas contribuir a este proyecto, por favor, abre un "issue" o envía un "pull request" en GitHub.

### Licencia

Este proyecto está bajo la licencia [Publica General GNU v3.0].
