from .base import *
from decouple import config

# Todo change database
Database
https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRESQL_DATABASE_NAME'),
        'USER': config('POSTGRESQL_DATABASE_USER'),
        'PASSWORD': config('POSTGRESQL_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
PARENT_HOST = '52.35.31.177'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://52.35.31.177"

PAYSTACK_LIVE_KEY = config('PAYSTACK_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY', default='')

