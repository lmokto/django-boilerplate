from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['127.0.0.1:8000']

# Application definition

THIRD_PARTY_APPS += ()

LOCAL_APPS += ()

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tests.db'),
    }
}
