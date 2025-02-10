# Proyecto App - Gestión Administrativa y Optimización de Recursos

## Descripción

Esta aplicación web está desarrollada utilizando Python y Flask, y tiene como objetivo permitir la gestión administrativa y la optimización de recursos de sistemas informáticos. La aplicación incluye funcionalidades para la gestión de usuarios, autenticación y administración de datos.

## Funcionalidades

1. **Página de Inicio:**
   - Muestra un saludo y una vista general de la aplicación.
   - Solo accesible después de iniciar sesión.

2. **Login:**
   - Permite a los usuarios autenticarse con su correo electrónico y contraseña.
   - Incluye una página para la recuperación de contraseña (si se implementa).

3. **Gestión de Usuarios:**
   - Permite ver todos los usuarios registrados en el sistema.
   - Los administradores pueden editar o eliminar usuarios.
   - Solo accesible para usuarios autenticados con el rol de administrador.

4. **Registro de Usuarios:**
   - Formulario de registro que permite a los nuevos usuarios crear una cuenta.
   - Validación de campos antes de enviar el formulario.
   - Integrado con Flask para almacenar la información en la base de datos.

## Requisitos

- Python 3.x
- MySQL (utilizado para la base de datos, se puede gestionar con XAMPP)
- Flask
- Otras dependencias necesarias (ver `requirements.txt`)

## Instalación
## Instalación de dependencias adicionales:
```bash
pip install psutil plyer


### 1. Clonar el repositorio

Clona el proyecto en tu máquina local:

```bash
git clone https://github.com/Andreas103-SI/ProyectoApp.git
cd proyecto_app
```

### 2. Crear un entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar la base de datos

Asegúrate de que MySQL está corriendo en XAMPP y crea una base de datos:

```sql
CREATE DATABASE proyecto_app;
```

Configura las credenciales de la base de datos en un archivo `.env`.

### 4. Ejecutar la aplicación

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.
