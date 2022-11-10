
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
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.sender.username

