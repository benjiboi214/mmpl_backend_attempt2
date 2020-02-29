"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import environ
import os
from ssm_parameter_store import EC2ParameterStore

ROOT_DIR = (
    environ.Path(__file__) - 4
)  # (configuration/api/settings/base.py - 3 = mmpl_backend/)
APPS_DIR = ROOT_DIR.path("api")

env = environ.Env(
    USE_DOCKER=(bool, False),
    DJANGO_READ_SSM_PARAMS=(bool, False)
)

if env.bool("DJANGO_READ_SSM_PARAMS"):
    store = EC2ParameterStore(
        aws_access_key_id=env("AWS_SSM_ACCESS_KEY"),
        aws_secret_access_key=env("AWS_SSM_SECRET_KEY"),
        region_name=env("AWS_DEFAULT_REGION")
    )
    parameters = store.get_parameters_by_path('/mmpl-backend/dev/', recursive=True)
    for key in parameters:
        os.environ[key] = parameters[key]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&nrl7c&sk)c%xwe++1ucpdc9@ip#k_&*ej%gi5@3rb92@x)@g^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = [
    "django-bluegreen-example-226063929.ap-southeast-2.elb.amazonaws.com",
    "staging.mmpl.systemiphus.com"
]

# From this package https://pypi.org/project/django-allow-cidr/
# On the advice of this article https://mozilla.github.io/meao/2018/02/27/django-k8s-elb-health-checks/
ALLOWED_CIDR_NETS = ['10.10.0.0/16', "127.0.0.0/16"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites'
]

MIDDLEWARE = [
    'allow_cidr.middleware.AllowCIDRMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuration.api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path("templates"))],
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

WSGI_APPLICATION = 'configuration.api.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR("staticfiles"))
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# AUTH SETTINGS
# Rest Auth Use djangorestframework-jwt package
REST_USE_JWT = True

# Needed after adding django.contrib.sites for some reason
SITE_ID = 1
