"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.dev20211231054910.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from mysite.settings.base import *
from pathlib import Path
import environ
import os

from dotenv import load_dotenv

load_dotenv()

env = environ.Env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-53th1vs%k)j1(q-j%z95yvs%!ls24%q0-2tt!3=#f7!z*n#b61'
# SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app']


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social_django',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    "django_extensions",
    "pwa"
   ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE= [
    'django.middleware.security.SecurityMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF= 'mysite.urls'

TEMPLATES= [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Python Social Auth Context Processors 
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION= 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS= [
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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE= 'en-us'

TIME_ZONE= 'UTC'

USE_I18N= True

USE_TZ= True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL= 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD= 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    # Facebook 
    'social_core.backends.facebook.FacebookOAuth2', 
    
    # Google 
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.google.GoogleOAuth2',
    # Django 
    'django.contrib.auth.backends.ModelBackend',
    # 'social_core.backends.google.GooglePlusAuth',
)

SOCIAL_AUTH_FACEBOOK_KEY = 963275077611461
# SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET ="64bd6ee74424038a29c55aaa244ec542"
# SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")



#SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/" 


SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'polls:admCliente'
LOGIN_URL = 'polls:entrar'
LOGOUT_URL = 'polls:salir'
LOGIN_REDIRECT_URL = 'polls:principal'
LOGOUT_REDIRECT_URL = 'polls:principal'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Mercado Pago

# env = environ.Env()
# env.read_env(str(BASE_DIR / ".env"))
# MERCADO_PAGO_PUBLIC_KEY = env("MERCADO_PAGO_PUBLIC_KEY")
# MERCADO_PAGO_ACCESS_TOKEN = env("MERCADO_PAGO_ACCESS_TOKEN")


#vendedor de prueba 
MERCADO_PAGO_PUBLIC_KEY = 'APP_USR-6eb7add2-a62a-4312-a74f-06c1e9646fc3'
MERCADO_PAGO_ACCESS_TOKEN = 'APP_USR-8847563472531392-021522-a4381f0595bf90e0ee6fa3b952f7d988-1075035405'


PWA_APP_NAME = "LSM Shop"
PWA_APP_DESCRIPTION = "Aplicación móvil información de negocios"
PWA_APP_THEME_COLOR = "#3477f5"
PWA_APP_BACKGROUND_COLOR = "#6699f7"
PWA_APP_START_URL = "/"
PWA_APP_ICONS = [
    {
        'src': '/static/pwa/img/AyM.png',
        'sizes': '500x500'
    },
    {
        "src": "/static/pwa/img/android-icon-36x36.png",
        "sizes": "36x36",
        "type": "image\/png",
        "density": "0.75"
    },
    {
        "src": "/static/pwa/img/android-icon-48x48.png",
        "sizes": "48x48",
        "type": "image\/png",
        "density": "1.0"
    },
    {
        "src": "/static/pwa/img/android-icon-72x72.png",
        "sizes": "72x72",
        "type": "image\/png",
        "density": "1.5"
    },
    {
        "src": "/static/pwa/img/android-icon-96x96.png",
        "sizes": "96x96",
        "type": "image\/png",
        "density": "2.0"
    },
    {
        "src": "/static/pwa/img/android-icon-144x144.png",
        "sizes": "144x144",
        "type": "image\/png",
        "density": "3.0"
    },
    {
        "src": "/static/pwa/img/android-icon-192x192.png",
        "sizes": "192x192",
        "type": "image\/png",
        "density": "4.0"
    }



]

PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/pwa/img/AyM.png',
        'sizes': '500x500'
    },
    {
        "src": "/static/pwa/img/apple-icon-57x57.png",
        "sizes": "57x57",
        "type": "image\/png",
        "density": "0.75"
    },
    {
        "src": "/static/pwa/img/apple-icon-60x60.png",
        "sizes": "60x60",
        "type": "image\/png",
        "density": "0.75"
    },
    {
        "src": "/static/pwa/img/apple-icon-72x72.png",
        "sizes": "72x72",
        "type": "image\/png",
        "density": "1.5"
    },
    {
        "src": "/static/pwa/img/apple-icon-76x76.png",
        "sizes": "76x76",
        "type": "image\/png",
        "density": "1.5"
    },
    {
        "src": "/static/pwa/img/apple-icon-114x114.png",
        "sizes": "114x114",
        "type": "image\/png",
        "density": "2.0"
    },
    {
        "src": "/static/pwa/img/apple-icon-120x120.png",
        "sizes": "120x120",
        "type": "image\/png",
        "density": "2.5"
    },
    {
        "src": "/static/pwa/img/apple-icon-144x144.png",
        "sizes": "144x144",
        "type": "image\/png",
        "density": "3.0"
    },
    {
        "src": "/static/pwa/img/apple-icon-152x152.png",
        "sizes": "152x152",
        "type": "image\/png",
        "density": "3.5"
    },
    {
        "src": "/static/pwa/img/apple-icon-180x180.png",
        "sizes": "180x180",
        "type": "image\/png",
        "density": "4.0"
    }

    
]

PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/pwa/img/favicon-96x96.png',
        'media': '(device-width: 320px) and (device-height:568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_LANG = 'es'
PWA_SERVICE_WORKER_PATH = "static/pwa/sw.js"
# PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'polls/static/js', 'sw.js')

