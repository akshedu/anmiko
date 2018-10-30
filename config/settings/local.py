from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='*x)1_h%%##ssx#)2buv30s95^wem6fbg0hdys8n6po*dbmbmm6')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'akshedu'
EMAIL_HOST_PASSWORD = env('GMAIL_APP_PASSWORD')