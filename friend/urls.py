from django.urls import path
from friend.views import (send_friend_request,
                          accept_friend_request,)

# https://www.youtube.com/watch?v=aGnQCsSwheE&list=RDCMUCoNZZLhPuuRteu02rh7bzsw&index=2

app_name = 'friend'
urlpatterns = [
    path('friend_request/<user_id>', send_friend_request, name='friend-request'),
    path('friend_request_accept/<user_id>/', accept_friend_request, name='friend-request-accept'),
]