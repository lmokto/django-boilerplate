from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '{{ secret_key }}'

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

# TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader

TEMPLATES[0]['APP_DIRS'] = False

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
