from django.urls import path
from friend.views import (send_friend_request, accept_friend_request,)

# https://www.youtube.com/watch?v=aGnQCsSwheE&list=RDCMUCoNZZLhPuuRteu02rh7bzsw&index=2

app_name = 'friend'
urlpatterns = [
    path('send_request/', send_friend_request, name='send_request'),
    path('accept_request/', accept_friend_request, name='accept_request'),
]