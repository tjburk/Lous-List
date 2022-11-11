from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FriendRequest, FriendList
from django.contrib import messages
from django.http import HttpResponse


def send_friend_request(request, username):
    sender = request.user
    receiver = User.objects.get(username=username)
    # Create friend lists for the sender and receiver if they don't have them already
    try:
        FriendList.objects.get(user=sender)
    except FriendList.DoesNotExist:
        FriendList.objects.create(user=sender)
    try:
        FriendList.objects.get(user=receiver)
    except FriendList.DoesNotExist:
        FriendList.objects.create(user=receiver)

    # Create a friend request if one doesn't already exist
    try:
        FriendRequest.objects.get(sender=sender, receiver=receiver)
        messages.warning(request, "Friend request already sent.")
        return redirect("profile")
    except FriendRequest.DoesNotExist:
        FriendRequest.objects.create(sender=sender, receiver=receiver)
        messages.success(request, "Friend request sent.")
        return redirect("profile")


def accept_friend_request(request, username):
    receiver = request.user
    sender = User.objects.get(username=username)
    try:
        friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver)
        # If the friend request exists, add friends to each other's friend lists and delete it
        # Accept friend request and update sender and receiver
        receiver.friendlist.add_friend(sender)
        sender.friendlist.add_friend(receiver)
        friend_request.delete()
        messages.success(request, "Friend request accepted.")
        return redirect("profile")
    except FriendRequest.DoesNotExist:
        messages.warning(request, "No friend request found.")
        return redirect("profile")


