from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
# http://www.miniwebtool.com/django-secret-key-generator

SECRET_KEY = None

ALLOWED_HOSTS = ['ip(s) y/o dominio(s), aquí']

# Application definition

THIRD_PARTY_APPS += ()

LOCAL_APPS += ()

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
