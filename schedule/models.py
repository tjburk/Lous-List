from django.contrib.auth.models import User
from list_classes.models import Course
from django.db import models


class Schedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="schedule")
    courses = models.ManyToManyField(Course, blank=True, related_name="courses")

    def __str__(self):
        return self.user.username

    def add_course(self, course):
        self.courses.add(course)
        self.save()

    def delete_course(self, course):
        self.courses.remove(course)
        self.save()

