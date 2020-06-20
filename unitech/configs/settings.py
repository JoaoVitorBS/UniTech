import os
from decouple import config, Csv
from dj_database_url import parse as dburl
from .configs import DEFAULT_DATABASE_URL, DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, \
    EMAIL_PORT, EMAIL_USE_TLS

APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(APP_ROOT))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# ALLOWED_HOSTS = ['', ]

if not DEFAULT_DATABASE_URL:
    DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(APP_ROOT, 'db.sqlite3')

# DATABASES = {
#   'default': config('DATABASE_URL', default=DEFAULT_DATABASE_URL, cast=dburl),
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_unitech',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # unitech apps:
    'unitech.apps.base',
    'unitech.apps.login',
    'unitech.apps.cadastro',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para paginas que exigem login
    'unitech.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'unitech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_ROOT, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # contexto para a versao do unitech
                'unitech.apps.base.context_version.unitech_version',
                # contexto para a foto de perfil do usuario
                'unitech.apps.login.context_user.foto_usuario',
            ],
        },
    },
]

WSGI_APPLICATION = 'unitech.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(APP_ROOT, 'static'),
]

MEDIA_ROOT = os.path.join(APP_ROOT, 'media/')
MEDIA_URL = 'media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_NOT_REQUIRED = (
    r'^/login/$',
    r'/login/esqueceu/',
    r'/login/trocarsenha/',
    r'/logout/',
)
