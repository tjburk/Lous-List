
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# https://www.youtube.com/watch?v=hyJO4mkdwuM


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        # Add a new friend
        if account not in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        # Remove a friend
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        # Unfriend someone
        remover_friends_list = self # Person terminating friendship

        # Remove friend from remover friend list
        remover_friends_list.remove_friend(removee)

        # Remove friend from removee friend list
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        # Return true if mutual friends
        if friend in self.friends.all():
            return True
        else:
            return False


# https://www.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield
@receiver(post_save, sender=FriendList)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        FriendList.objects.create(user=instance)
    instance.user.save()


class FriendRequest(models.Model):
    # Friend request consists of 2 parts
    # 1. A sender
    # 2. A receiver
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", default=None)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", default=None)

    def __str__(self):
        return self.sender.username

    def accept(self):
        # Accept friend request and update sender and receiver
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
