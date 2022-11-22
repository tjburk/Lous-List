from django.urls import path
from friend.views import (send_friend_request, accept_friend_request, get_all_users)

app_name = 'friend'
urlpatterns = [
    path('send_request/<user_id>', send_friend_request, name='send_request'),
    path('accept_request/<user_id>', accept_friend_request, name='accept_request'),
    path('all_users/', get_all_users, name='user_page'),
]