from django.contrib import admin
from picwall.models import Picture, PictureComment, PhotoWall, PhotoInformation

admin.site.register(Picture)
admin.site.register(PictureComment)
admin.site.register(PhotoWall)
admin.site.register(PhotoInformation)
