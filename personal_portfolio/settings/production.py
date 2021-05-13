from .base import *  # noqa: F401 F403
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['kudlanov-django.herokuapp.com', 'www.kudlanov-django.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# File Storage: Google Cloud Storage
DEFAULT_FILE_STORAGE = 'gcloud.GoogleCloudMediaFileStorage'
STATICFILES_STORAGE = 'gcloud.GoogleCloudStaticFileStorage'

GS_PROJECT_ID = 'kudlanov-portfolio'
GS_STATIC_BUCKET_NAME = 'kudlanov.com'

STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
MEDIA_ROOT = "media/"

UPLOAD_ROOT = 'media/uploads/'

DOWNLOAD_ROOT = os.path.join(BASE_DIR, "media/downloads")  # noqa: F405
DOWNLOAD_URL = MEDIA_URL + "downloads/"

# Security Settings
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
