from django.urls import path
from friend.views import send_friend_request

# https://www.youtube.com/watch?v=aGnQCsSwheE&list=RDCMUCoNZZLhPuuRteu02rh7bzsw&index=2

app_name = 'friend'
urlpatterns = [
    path('friend_request/', send_friend_request, name='friend request'),
    ]