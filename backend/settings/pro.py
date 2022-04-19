from .base import *

DEBUG = False

# upisati domen od sajta
ALLOWED_HOSTS = ['*']


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
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