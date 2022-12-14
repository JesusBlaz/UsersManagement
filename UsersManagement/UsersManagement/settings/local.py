from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

