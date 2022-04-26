from .base import *

# kada stavim na false, ne servuje static files, mora heroku da ih servuje (videti to)
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True
# upisati domen od sajta
ALLOWED_HOSTS = ['trainingplanapi.herokuapp.com', '127.0.0.1']


CORS_ALLOWED_ORIGINS = ["https://guarded-falls-39745.herokuapp.com",
                 "http://guarded-falls-39745.herokuapp.com"]

# White listing the localhost:3000 port
# for React
CORS_ORIGIN_WHITELIST = [
    "https://guarded-falls-39745.herokuapp.com",
    "http://guarded-falls-39745.herokuapp.com"
]

# trazi varijablu database url na heroku i povezuje se na produkcijsku bazu
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

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = ''



# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)