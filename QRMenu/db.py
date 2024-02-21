import os 
import dj_database_url

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE":'django.db.backends.sqlite3',
        "NAME": BASE_DIR / 'db.sqlite3',
    }
}

DATABASES["default"] = dj_database_url.parse("postgres://qrmenu_django_render_user:6n26PdpMLl00ZChlixNi5FaHKaQ6e6Vs@dpg-cn9p3docmk4c73a1d310-a.oregon-postgres.render.com/qrmenu_django_render")

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'QRMenu',      # Nombre de tu base de datos
        'USER': 'postgres',     # Nombre de usuario de PostgreSQL
        'PASSWORD': 'brunoPtah300',     # Contraseña de usuario de PostgreSQL
        'HOST': 'localhost',             # Dirección del host de la base de datos (puede ser 'localhost' si está en tu máquina)
        'PORT': '5432',                  # Puerto en el que PostgreSQL está escuchando (predeterminado: 5432)
    }
}
