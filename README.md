# Proyecto App - Gestión Administrativa y Optimización de Recursos

## Descripción

Esta aplicación web está desarrollada utilizando Python y Flask, y tiene como objetivo permitir la gestión administrativa y la optimización de recursos de sistemas informáticos. La aplicación incluye funcionalidades para la gestión de usuarios, autenticación, administración de datos, monitoreo y optimización de procesos del sistema.

## Funcionalidades

### 1. Gestión de Usuarios
- Permite ver todos los usuarios registrados en el sistema.
- Los administradores pueden editar o eliminar usuarios.
- Solo accesible para usuarios autenticados con el rol de administrador.

### 2. Autenticación de Usuarios
- Permite a los usuarios iniciar sesión con su correo electrónico y contraseña.
- Registro de nuevos usuarios con validación de datos.
- Posibilidad de recuperación de contraseña (si se implementa).

### 3. Monitoreo de Recursos del Sistema
- Visualización en tiempo real del uso de CPU, memoria y almacenamiento.
- Endpoint disponible en `http://127.0.0.1:5000/monitor` para obtener los datos en formato JSON.
- Vista HTML disponible en `http://127.0.0.1:5000/monitor_view` para una interfaz gráfica.

### 4. Optimización de Procesos
- Detección de procesos ineficientes basados en el uso de CPU y memoria.
- Opción de optimización automática al terminar procesos problemáticos.
- Notificación al administrador en caso de sobrecarga de recursos (opcional si se configura el envío de emails).
- Endpoint disponible en `http://127.0.0.1:5000/optimizer`.

## Requisitos

- Python 3.x
- MySQL (utilizado para la base de datos, se puede gestionar con XAMPP)
- Flask
- Dependencias adicionales (ver `requirements.txt`)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Andreas103-SI/ProyectoApp.git
cd proyecto_app
```

### 2. Crear un entorno virtual e instalar dependencias

```bash
python -m venv venv
<<<<<<< HEAD
venv\Scripts\activate  # En Windows
=======
source venv/bin/activate 
>>>>>>> 6c29cb27a6d4f03663621345fa743b210a9c127c
pip install -r requirements.txt
```

### 3. Instalar dependencias adicionales

```bash
pip install psutil plyer
```

### 4. Configurar la base de datos

Asegúrate de que MySQL está corriendo en XAMPP y crea una base de datos:

```sql
CREATE DATABASE proyecto_app;
```

Configura las credenciales de la base de datos en un archivo `.env`.

### 5. Ejecutar la aplicación

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Notas

- El archivo `.gitignore` está configurado para excluir archivos innecesarios, como `__pycache__` y el entorno virtual `venv`.
- El monitoreo de recursos y la optimización de procesos están implementados, pero el envío de notificaciones está deshabilitado hasta configurar la autenticación de usuarios.
- Se recomienda actualizar `pip` a la última versión con:

```bash
python -m pip install --upgrade pip
