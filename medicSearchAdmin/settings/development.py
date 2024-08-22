from .settings import*
import os

DEBUG = True

# Criar a secret key para seu ambiente de desenvolvimento
SECRET_KEY='as78df6as89df76a9s87g6as789dg6as9d78g1'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}