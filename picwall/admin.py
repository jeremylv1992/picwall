from django.contrib import admin
from picwall.models import pw_pic, pic_comment, PhotoWall, PhotoInformation


admin.site.register(pw_pic)
admin.site.register(pic_comment)
admin.site.register(PhotoWall)
admin.site.register(PhotoInformation)
