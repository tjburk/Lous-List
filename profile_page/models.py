from django.db import models

from django.contrib.auth.models import User
from list_classes.models import Course


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("Student", on_delete=models.CASCADE)
    schedule = models.ManyToManyField(Course, on_delete=models.CASCADE)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

