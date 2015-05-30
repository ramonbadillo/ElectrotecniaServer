"""
Django settings for electrotecnia project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 1.8.2.
=======
Generated by 'django-admin startproject' using Django 1.8.
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'vm#1swe*(ta=a&+gu75+4g(m%h(vhj9@mb1v&zl(5ci&5we2o)'
=======
SECRET_KEY = '(xhm!d1y(2^&q5!fe73_i-naam*-x_a*)4taa$rkak^2lz!tq='
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
<<<<<<< HEAD
    #Framework APPS
=======
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'django.contrib.sites',

    #3RD PARTY APPS
    'rest_framework',
    'registration',
    'crispy_forms',

    #MY APPS :)
    'devices',
    'records',


=======
    'devices',
    'gadgets',
    'registrys',
    #'userprofiles',
    'rest_framework',
    'bootstrapform',
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'electrotecnia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [os.path.join(BASE_DIR,"templates")],
=======
        'DIRS': [],
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'electrotecnia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

<<<<<<< HEAD
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
'''
DATABASES = {
'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9bcde5096k0og',
        'USER': 'synwacqamigvrd',
        'PASSWORD': 'c9O9RS18z5J2EQRH37IVjiMfn_',
        'HOST': 'ec2-107-21-114-132.compute-1.amazonaws.com', # Or something like this
        'PORT': '5432',
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'dfgekrk78a8rgg',                     
        'USER': 'wutxhrdnnawyah',
        'PASSWORD': 'mup8l1DHf7DNs8imZiiROBmnwY',
        'HOST': 'ec2-54-163-235-165.compute-1.amazonaws.com', # Or something like this
        'PORT': '5432',                     
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


# https://docs.djangoproject.com/en/1.8/howto/static-files/


<<<<<<< HEAD
SITE_NAME = 'Electrotecnia'
=======
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81




# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_STORAGE = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

<<<<<<< HEAD
#API SETTINGS
=======

>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
<<<<<<< HEAD

=======
 
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
<<<<<<< HEAD

=======
        
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
    ]
}
REST_SESSION_LOGIN = False
#AUTHENTICATION_BACKENDS = (
#    'userprofiles.backends.EmailBackend',

#)

<<<<<<< HEAD

#CRYSPY SETTINGS

CRISPY_TEMPLATE_PACK = 'bootstrap3'


#REDUX SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
=======
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81