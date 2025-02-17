import os

env = os.getenv('DJANGO_ENV', 'local')

if env == 'local':
    from .local import *
else:
    from .base import *
