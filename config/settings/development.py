from .base import *  # noqa

from datetime import timedelta

import environ


env = environ.Env()
environ.Env.read_env()  
# Asosiy sozlamalar
ALLOWED_HOSTS = ['*']
DEBUG = True
INTERNAL_IPS = ["127.0.0.1"]

# Debug Toolbar ni faollashtirish
INSTALLED_APPS += ["debug_toolbar",'users']  # Debug Toolbar ni ishlatish uchun
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # Debug Middleware qo'shish

# Ma'lumotlar bazasi konfiguratsiyasi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",  # Ma'lumotlar bazasi fayli
    }
}


# Atrof-muhit o'zgaruvchilarini ishlatish
AUTH_USER_MODEL = 'users.User'

# Email sozlamalari (Gmail orqali)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# JWT (JSON Web Token) konfiguratsiyasi
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  
}
