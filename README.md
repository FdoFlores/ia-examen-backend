# ia examen backend

# Requerimientos
- Docker
- Python
- 

# Instrucciones para correr el proyecto.

## Inicializar el docker con docker compose
    sudo docker compose up -d
    
## Instalamos python venv
    sudo apt install python3.12-venv

## Inicializamos el virtual environment
    python -m venv venv
## activamos el venv
    source venv/bin/activate

## Instalamos paquetes
    pip install -r requirements.txt

    pip install psycopg2 # for windows
    pip install psycopg2-binary # for linux

## Correr migraciones
    python manage.py makemigrations
    python manage.py migrate

## Poblar catalogos en DB
    python manage.py seed_all

## Correr el proyecto
    python manage.py runserver