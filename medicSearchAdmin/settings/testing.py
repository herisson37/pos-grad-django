from .settings import*
import os

DEBUG = True

# Criar a secret key para seu ambiente de desenvolvimento
SECRET_KEY='as78df6as89df76a9s87g6as789dg6as9d78g3'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Nome do seu banco de dados',
        'USER': 'Nome do usuario',
        'PASSWORD': 'Sua senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}