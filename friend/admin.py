from django.contrib import admin

from .models import FriendList, FriendRequest

admin.site.register(FriendRequest)
admin.site.register(FriendList)