from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ptqhp@=%x#r+4@(_(t^suwwjg3a2-=!apzkot7-8n3syn_4_j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'USER': 'django',
        'HOST': 'db',
        'PORT': '3306',
        'NAME': 'django_test',
        'PASSWORD': 'secret',
    }
}
