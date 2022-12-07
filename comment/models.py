from django.db import models
from list_classes.models import Course
from schedule.models import Schedule
from django.contrib.auth.models import User
from django.urls import reverse


class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"%s" by %s - %s' % (self.course.description, self.course.instructor_name, self.name)

    def get_absolute_url(self):
        return reverse('list_classes:description', kwargs={'course_number': self.course.course_number})
