import os

import dj_database_url
from unipath import Path


BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'rdyupsnp6@)2cus@6n)r_zfn&ly$zwp(a!&o4_ah__%j%0w7qr'

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['*'])

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
]

LOCAL_APPS = [
    'comun',
    'usuario',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

DJANGO_CONTEXT_PROCESSORS = [
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

THIRD_PARTY_CONTEXT_PROCESSORS = []

LOCAL_CONTEXT_PROCESSORS = []

CONTEXT_PROCESSORS = DJANGO_CONTEXT_PROCESSORS \
    + THIRD_PARTY_CONTEXT_PROCESSORS + LOCAL_CONTEXT_PROCESSORS

TEMPLATES_DIRS = [
    BASE_DIR.child('tickets').child('templates'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': CONTEXT_PROCESSORS,
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database

DEFAULT_DATABASE = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=DEFAULT_DATABASE)
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.ancestor(2).child('static')

STATICFILES_DIRS = (
    BASE_DIR.ancestor(1).child('static'),
)

# Media

MEDIA_ROOT = BASE_DIR.ancestor(2).child('media')

MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True
