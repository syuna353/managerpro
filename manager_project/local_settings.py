import os

SECRET_KEY = '52x=8c0ophvbgu=)f(turv(lo+tw(xz__c0q02_+a3yzma!v(q'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
