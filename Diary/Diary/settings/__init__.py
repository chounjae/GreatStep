import os

env = os.getenv('DJANGO_ENV', 'host')

if env == 'host':
    from .host import *
else:
    from .base import *