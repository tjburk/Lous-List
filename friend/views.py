from django.shortcuts import render, redirect
from .models import FriendRequest, FriendList
from django.contrib import messages
from django.contrib.auth.models import User


def send_friend_request(request, user_id):
    sender = request.user
    receiver = User.objects.get(id=user_id)
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
        messages.success(request, "Friend request already sent.")
        return redirect("friend:user_page")
    except FriendRequest.DoesNotExist:
        FriendRequest.objects.create(sender=sender, receiver=receiver)
        messages.success(request, "Friend request sent.")
        return redirect("friend:user_page")


def accept_friend_request(request, user_id):
    receiver = request.user
    sender = User.objects.get(id=user_id)
    if sender in receiver.friends.all():
        messages.success(request, "Already friends.")
        return redirect("friend:user_page")
    try:
        friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver)
        # If the friend request exists, add friends to each other's friend lists and delete it
        # Accept friend request and update sender and receiver
        receiver.friendlist.add_friend(sender)
        sender.friendlist.add_friend(receiver)
        friend_request.delete()
        messages.success(request, "Friend request accepted.")
        try:
            friend_request = FriendRequest.objects.get(sender=receiver, receiver=sender)
            friend_request.delete()
        except FriendRequest.DoesNotExist:
            pass
        return redirect("friend:user_page")
    except FriendRequest.DoesNotExist:
        messages.success(request, "No friend request found.")
        return redirect("friend:user_page")


def get_all_users(request):
    # Set up context variables
    if request.user.is_authenticated:
        # All Users
        users = User.objects.all()

        # All people that have sent requests to user
        received_friend_requests = FriendRequest.objects.filter(receiver=request.user)
        received_users = []
        for friend_request in received_friend_requests:
            received_users.append(friend_request.sender)

        # All people that current user has sent friends requests to
        sent_friend_requests = FriendRequest.objects.filter(sender=request.user)
        sent_users = []
        for friend_request in sent_friend_requests:
            sent_users.append(friend_request.receiver)

        # All user's friends
        friends = []
        friend_list_query = request.user.friends.all()
        for friend_list in friend_list_query:
            friends.append(friend_list.user_id)

        return render(request, 'friend/all_users_new.html', {'users': users,
                                                             'received_users': received_users,
                                                             'sent_users': sent_users,
                                                             'friends': friends})
    else:
        return render(request, 'friend/all_users_new.html')



