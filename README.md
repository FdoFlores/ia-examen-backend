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

## Poblar catalogos en DB para que funcione el proyecto correctamente
    python manage.py seed_all

## Correr el proyecto
    python manage.py runserver

## Testing
    pytest

### Pueden revisar el proyecto desplegado en una instancia aws ec2 en:
http://18.117.255.6:8000


# Descripción del proyecto
    El proyecto reino del trebol procesa solicitudes de registro de magos, los cuales se registran con un nombre, apellido, edad y deben solicitar una afinidad magica.
    Una vez hecha la solicitud deben actualizar su status con el endpoint patch, el cual idealmente en un ambiende de producción lo utilizaría un administrador para aceptar o rechazar magos.
    Una vez que se acepta la solicitud de ingreso del mago se le asigna un grimorio aleatoriamente.
    
    La asignación de grimorios es aleatoria, cada tipo de grimorio tiene una distinta probabilidad de ser asignado según su rareza.
    Trebol de una hoja: 40%
    Trebol de dos hojas: 30%
    Trebol de tres hojas: 15%
    Trebol de cuatro hojas: 10%
    Trebol de cinco hojas: 5%

# Entregables del proyecto alcanzados.
    Python
    Django
    PostgreSQL
    Pytest
    Documentación con swagger # http://18.117.255.6:8000/docs
    Dockerización
    Interfaz web

### Este proyecto no utiliza ningun tipo de token, autenticación o autorización de usuarios.