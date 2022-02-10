BACKEND = 'mysql'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pivot',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

INSTALLED_APPS = (
    'django_pivot.tests.pivot',
)

SITE_ID = 1,

SECRET_KEY = 'secret'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)
