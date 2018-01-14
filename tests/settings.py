INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'social_django',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

SECRET_KEY = 'test'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
]
