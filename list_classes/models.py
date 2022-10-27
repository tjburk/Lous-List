from django.db import models
from django.contrib import admin
from datetime import datetime, date

from django.urls import reverse


class Course(models.Model):
    # Instructor
    instructor_name = models.CharField(max_length=50, blank=True)
    instructor_email = models.CharField(max_length=50, blank=True)
    course_number = models.IntegerField(primary_key=True)   # Unique course number
    semester_code = models.IntegerField(null=True, blank=True)   # Code for semester (always starts with 1)
    subject = models.CharField(max_length=4, blank=True)    # Mnemonic of class (ex: "CS" 1010)
    catalog_number = models.IntegerField(null=True, blank=True)  # Number of class (ex: CS "1010")
    description = models.CharField(max_length=500)  # Name of class
    units = models.CharField(max_length=10, blank=True)  # Number of units (string)
    component = models.CharField(max_length=10, blank=True)  # LEC,DIS,etc.
    class_capacity = models.IntegerField(null=True, blank=True)
    wait_list = models.IntegerField(null=True, blank=True)
    wait_cap = models.IntegerField(null=True, blank=True)
    enrollment_total = models.IntegerField(null=True, blank=True)
    enrollment_available = models.IntegerField(null=True, blank=True)
    topic = models.CharField(max_length=50, blank=True)  # Not sure - usually empty string
    # Meetings
    meetings_days = models.CharField(max_length=10, blank=True)  # "MoWe" "TuTh" etc.
    meetings_start_time = models.CharField(max_length=500, blank=True)  # "17.00.00.000000-05:00"
    meetings_end_time = models.CharField(max_length=500, blank=True)  # "18.15.00.000000-05:00",
    meetings_facility_description = models.CharField(max_length=500, blank=True)  # "Olsson Hall 009"

    def __str__(self):
        return self.description


class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"%s" by %s - %s' % (self.course.description, self.course.instructor_name, self.name)

    def get_absolute_url(self):
        return reverse('list_classes:classes')
