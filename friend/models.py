from django.contrib.auth.models import User
from django.db import models


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="friendlist")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, user):
        if user not in self.friends.all():
            self.friends.add(user)
            self.save()


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.sender.username + " to " + self.receiver.username

