from .base import *  # noqa
from .base import env

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DJANGO_DB_NAME"),
        'USER': env("DJANGO_DB_USER"),
        'PASSWORD': env("DJANGO_DB_PASS"),
        'HOST': env("DJANGO_DB_HOST"),
        'PORT': env("DJANGO_DB_PORT"),
    }
}
