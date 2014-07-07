#-*- coding:utf-8 -*-
import os
import sys
 
os.environ.setdefault(['DJANGO_SETTINGS_MODULE'], 'mysite.settings')
 
path = os.path.dirname(os.path.abspath(__file__)) + '/mysite'
if path not in sys.path:
    sys.path.insert(1, path)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
