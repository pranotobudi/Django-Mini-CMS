from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q%h$n5x$7di0v8m9uy9*1qxf@ph#t+yxd%7qz+#)9u$8_i#usj'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangominicms',
        'USER': 'djangominicms',
        'PASSWORD': 'passworddjangominicms',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
