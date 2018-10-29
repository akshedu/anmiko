from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='*x)1_h%%##ssx#)2buv30s95^wem6fbg0hdys8n6po*dbmbmm6')

DEBUG = env.bool('DJANGO_DEBUG', default=True)