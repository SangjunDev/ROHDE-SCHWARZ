from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'ROHDE&SCHWARZ3',
        'USER':'sangjunkim',
        'PASSWORD': '1234qwer',
        'HOST': 'localhost',
        'PORT':'5432',
        
    }
}
