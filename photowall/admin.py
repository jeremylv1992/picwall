from django.contrib import admin
from photowall.models import Picture, PictureComment, PhotoWall, PhotoInformation, PhotoInformation, WebSiteUser, PictureLabel, AskForFriendMessage

admin.site.register(Picture)
admin.site.register(PictureComment)
admin.site.register(PhotoWall)
admin.site.register(PhotoInformation)
admin.site.register(WebSiteUser)
admin.site.register(PictureLabel)
admin.site.register(AskForFriendMessage)
