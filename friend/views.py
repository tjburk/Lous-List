from django.shortcuts import render

from django.http import HttpResponse
import json

from django.contrib.auth.models import User
from friend.models import FriendList, FriendRequest

# https://www.youtube.com/watch?v=aGnQCsSwheE&list=RDCMUCoNZZLhPuuRteu02rh7bzsw&index=2


def send_friend_request(request):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = User.objects.get(pk=user_id)
            try:
                # Get all friend requests (active and non-active)
                friend_requests = FriendRequest.objects.filter(sender=user, receiver=receiver)
                # Find if any are active
                try:
                    for request in friend_requests:
                        if request.is_active:
                            raise Exception("You already sent them a friend request.")
                    # If none are active, then create a new friend request
                    friend_request = FriendRequest(sender=user, receiver=receiver)
                    friend_request.save()
                    payload['response'] = "Friend request sent."
                except Exception as e:
                    payload['response'] = str(e)
            except FriendRequest.DoesNotExist:
                # There are no friend requests, so create one
                friend_request = FriendRequest(sender=user, receiver=receiver)
                friend_request.save()
                payload['response'] = "Friend request sent."
            if payload['response'] is None:
                payload['response'] = "Something went wrong."
        else:
            payload['response'] = "Unable to send a friend request."
    else:
        payload['response'] = "You must be authenticated to send a friend request."
    return HttpResponse(json.dumps(payload), content_type="application/json")
