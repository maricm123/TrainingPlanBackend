from .base import *

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True
# upisati domen od sajta
ALLOWED_HOSTS = ['trainingplanapi.herokuapp.com']


CORS_ALLOWED_ORIGINS = ["https://guarded-falls-39745.herokuapp.com",
                 "http://guarded-falls-39745.herokuapp.com"]

# White listing the localhost:3000 port
# for React
CORS_ORIGIN_WHITELIST = [
    "https://guarded-falls-39745.herokuapp.com",
    "http://guarded-falls-39745.herokuapp.com"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgresql-concave-49155',
        'USER': 'frurrfhyhtwsqk',
        'PASSWORD': 'e15a3643937171e7469a99bd8059e2542719978fa86b83111c688086a5302027',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age = 600)
DATABASES['default'].update(db_from_env)

ROOT_URLCONF = 'backend.urls'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
   
}



# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'sanjamuskistudio@gmail.com'
# EMAIL_HOST_PASSWORD = 'mseghbfkcnatsctr'
# EMAIL_USE_TLS = True