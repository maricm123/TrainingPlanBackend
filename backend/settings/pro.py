from .base import *

DEBUG = True
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
        
    }
}

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