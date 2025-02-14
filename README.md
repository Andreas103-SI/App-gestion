# Proyecto App - Gestión Administrativa y Optimización de Recursos

## Descripción

Esta aplicación web está desarrollada utilizando Python y Flask. Su objetivo es facilitar la gestión administrativa y la optimización de recursos en sistemas informáticos. La aplicación incluye funcionalidades para la gestión de usuarios, autenticación, monitoreo de recursos, optimización de procesos y generación de informes detallados.

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

## Requisitos

- Python 3.x
- MySQL (se puede gestionar con XAMPP)
- Flask
- Dependencias adicionales (ver `requirements.txt`)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Andreas103-SI/ProyectoApp.git
cd proyecto_app
