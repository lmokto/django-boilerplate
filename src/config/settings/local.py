from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

THIRD_PARTY_APPS += (
    'debug_toolbar',
    'django_extensions',
)

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