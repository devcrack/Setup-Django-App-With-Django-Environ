import os
import enum
import nexmo
import environ


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_DIR = BASE_DIR.join('templates')



env_file = os.path.join(BASE_DIR, ".env")
env = environ.Env(
    # set casting and a default value
    DEBUG=(bool, False)
)


# Reading  env file
environ.Env.read_env(env_file)
# False if not in os.environ
DEBUG = env('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

EMAIL_BACKEND = env.EMAIL_SCHEMES['smtp']
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')

EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

DATABASES = {
    'default': env.db(engine='django.db.backends.postgresql_psycopg2'),
}
