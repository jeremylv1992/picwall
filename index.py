#-*- coding:utf-8 -*-
import sys
import os

os.environ.setdefault(['DJANGO_SETTINGS_MODULE'], 'mysite.settings')

from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
		 
application = WSGIApplication(WSGIHandler())
