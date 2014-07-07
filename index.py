#-*- coding:utf-8 -*-
from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
		 
application = WSGIApplication(WSGIHandler())
