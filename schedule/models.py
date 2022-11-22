from django.contrib.auth.models import User
from list_classes.models import Course
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Schedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="schedule")
    courses = models.ManyToManyField(Course, blank=True, related_name="courses")

    def __str__(self):
        return self.user.username

    def add_course(self, course_number):
        course = Course.objects.get(course_number=course_number)
        self.courses.add(course)
        self.save()

    def delete_course(self, course_number):
        course = Course.objects.get(course_number=course_number)
        self.courses.remove(course)
        self.save()

