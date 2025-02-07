# Proyecto App - Gestión Administrativa y Optimización de Recursos

## Descripción

Esta aplicación web está desarrollada utilizando Python y Flask, y tiene como objetivo permitir la gestión administrativa y la optimización de recursos de sistemas informáticos. La aplicación incluye funcionalidades para la gestión de usuarios, autenticación, y administración de datos.

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

## Requisitos

- Python 3.x
- MySQL (utilizado para la base de datos, se puede gestionar con XAMPP)
- Flask
- Otras dependencias necesarias (ver `requirements.txt`)

## Instalación

### 1. Clonar el repositorio

Clona el proyecto en tu máquina local:

```bash
git https://github.com/Andreas103-SI/ProyectoApp.git
cd proyecto_app
