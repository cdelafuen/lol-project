"""
WSGI config for lol project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from sys import path as syspath
from os import path as ospath
import os
from django.core.handlers.wsgi import WSGIHandler

apache_configuration = ospath.dirname(__file__)
workspace = ospath.dirname(apache_configuration)
syspath.append(workspace)
root = ospath.dirname(ospath.dirname(apache_configuration))
syspath.append(root)

syspath.append(apache_configuration)

_application = WSGIHandler()
def application(apache_environ, start_response):
  os.environ['DJANGO_SETTINGS_MODULE'] = apache_environ['DJANGO_SETTINGS_MODULE']
  return _application(apache_environ, start_response)