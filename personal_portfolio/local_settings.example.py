import os
import environ

# Have this file right next to the main settings.py file in the same directory

# Locally run commands in terminal like this, declaring ENV_PATH environment variable
# ENV_PATH=./personal_portfolio/.env python manage.py runserver

env = environ.Env()
ENV_PATH = './.env'
environ.Env.read_env(ENV_PATH)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
