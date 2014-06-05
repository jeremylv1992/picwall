#########################################################################
# File Name: admin.py
# Author: Jeremy
# mail: Jeremy19921115@gmail.com
# Created Time: Sat 31 May 2014 08:34:35 PM CST
#########################################################################
#!/usr/bin/env python
#coding=utf-8

from django.contrib import admin
from picwall.models import pw_pic, pic_comment, PhotoWall, PhotoInformation


admin.site.register(pw_pic)
admin.site.register(pic_comment)
admin.site.register(PhotoWall)
admin.site.register(PhotoInformation)
