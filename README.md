# Ecommerce Project

## Descripción

Este es un proyecto de ecommerce desarrollado con Python y Django. El proyecto permite a los usuarios navegar por productos, agregar productos al carrito de compras 

## Requisitos

- Python 3.x
- virtualenv

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local.

### 1. Clona el repositorio

### 2. Crea y activa un entorno virtual
python -m venv env
source env/bin/activate  

### 3. Instala las dependencias
pip install -r requirements.txt

### 4. Configura la base de datos
python manage.py migrate

### 6. Ejecuta el servidor de desarrollo
python manage.py runserver