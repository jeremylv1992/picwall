#-*- coding:utf-8 -*-
import sys
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
path = os.path.dirname(os.path.abspath(__file__)) + '/mysite'
if path not in sys.path:
    sys.path.insert(1, path)

from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
		 
application = WSGIApplication(WSGIHandler())
