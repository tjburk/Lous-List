from django.shortcuts import render
from django.contrib.auth.models import User

def allUsers(request):
    users=User.objects.all()
    return render(request, 'account/friends.html',{'users':users})