import os 
import dj_database_url

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qrmenu1',      # Nombre de tu base de datos
        'USER': 'postgres',     # Nombre de usuario de PostgreSQL
        'PASSWORD': '123',     # Contraseña de usuario de PostgreSQL
        'HOST': 'localhost',             # Dirección del host de la base de datos (puede ser 'localhost' si está en tu máquina)
        'PORT': '5432',                  # Puerto en el que PostgreSQL está escuchando (predeterminado: 5432)
    }
}
