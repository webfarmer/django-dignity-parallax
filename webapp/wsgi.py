"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.handlers.wsgi import WSGIHandler

sys.path = ['/root/sites/www.redspring.co.za/',] + sys.path

application = WSGIHandler()


#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
