from .base import *
import django_heroku  

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['django-mini-cms.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5cts1kaqniiqc',
        'USER': 'kbwmtpsuqjalnq',
        'PASSWORD': '278700edc7f2daed1cb168cc699ba61fd2447cdb643f93e957fb568f8ac6ad72',
        'HOST': 'ec2-107-20-185-27.compute-1.amazonaws.com',
        'PORT': '5432',        
    }
}

AWS_ACCESS_KEY_ID =  "AKIAIGUNMG5H4WWNAIAA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'django-mini-cms'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
django_heroku.settings(locals())