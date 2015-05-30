"""
WSGI config for electrotecnia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
<<<<<<< HEAD
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electrotecnia.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
=======

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electrotecnia.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
