from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!n6owtz8crs1)f-o(6^--8oo4t(9tbnzrwlu%#_3m2pv%x2^l1'

# Application definition

THIRD_PARTY_APPS += (
    # 'debug_toolbar',
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
