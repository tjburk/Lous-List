from django.contrib.auth.models import User
from .models import FriendRequest, FriendList
from django.contrib import messages
from django.shortcuts import redirect


def send_friend_request(request, user_id):
    sender = request.user
    receiver = User.objects.get(id=user_id)
    request = FriendRequest.objects.get(sender=sender, receiver=receiver)
    if request:
        messages.warning(request, "Friend request already sent.")
    else:
        FriendRequest.objects.create(sender=sender, receiver=receiver)
        messages.success(request, "Friend request sent.")


def accept_friend_request(request, user_id):
    receiver = request.user
    sender = User.objects.get(id=user_id)
    request = FriendRequest.objects.get(sender=sender, receiver=receiver)
    if request:
        # If the friend request exists, add friends to each other's friend lists and delete it
        # Accept friend request and update sender and receiver
        receiver_friend_list = FriendList.objects.get(user=receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(sender)
            sender_friend_list = FriendList.objects.get(user=sender)
            if sender_friend_list:
                sender_friend_list.add_friend(receiver)
        request.delete()
        messages.success(request, "Friend request accepted.")
    else:
        messages.warning(request, "No friend request found.")



