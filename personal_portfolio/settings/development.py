from .base import *  # noqa: F401 F403

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# File Storage: whitenoise for local server
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # noqa: F405
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # noqa: F405
MEDIA_URL = '/media/'

UPLOAD_ROOT = os.path.join(BASE_DIR, 'media/uploads')  # noqa: F405

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
