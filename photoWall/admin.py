from django.contrib import admin
from photoWall.models import User, Picture, PhotoWall, PhotoInformation

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(PhotoWall)
admin.site.register(PhotoInformation)
