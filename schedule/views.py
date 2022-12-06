from django.shortcuts import render, redirect
from list_classes.models import Course
from django.contrib import messages
from schedule.models import Schedule
from django.contrib.auth.models import User
import numpy as np


def get_schedule_courses(request, user_id):
    # If schedule doesn't exist, create one
    user = User.objects.get(id=user_id)
    try:
        Schedule.objects.get(user=user)
    except Schedule.DoesNotExist:
        Schedule.objects.create(user=user)

    # All user's courses in schedule
    schedule_courses = []
    course_list_query = user.schedule.courses.all()
    for course_list in course_list_query:
        course = Course.objects.get(course_number=course_list.course_number)
        schedule_courses.append(course)

    return schedule_courses


def add_course_to_schedule(request, course_number):
    # If schedule doesn't exist, create one
    user = request.user
    try:
        Schedule.objects.get(user=user)
    except Schedule.DoesNotExist:
        Schedule.objects.create(user=user)

    # Add course if it doesn't exist
    current_schedule = request.user.schedule
    course = Course.objects.get(course_number=course_number)
    # Does the course exist?
    if current_schedule.courses.filter(course_number=course_number).exists():
        messages.warning(request, "Course already in schedule.")
        # Refresh current page
        return redirect(request.META.get('HTTP_REFERER'))
    
    # If course times overlap
    course_days=course.meetings_days
    course_time_start=course.meetings_start_time
    course_time_end=course.meetings_end_time

    course_list_query = user.schedule.courses.all()
    for course_list in course_list_query:
        course_in_list = Course.objects.get(course_number=course_list.course_number)
        if(course_in_list.meetings_days in course_days) or (course_days in course_in_list.meetings_days):
            listCourse_time_start=course_in_list.meetings_start_time
            listCourse_time_end=course_in_list.meetings_end_time
            
            temp=3
            a=float(course_time_start[0:2]+"."+course_time_start[3:5])
            b=float(course_time_end[0:2]+"."+course_time_end[3:5])

            c=float(listCourse_time_start[0:2]+"."+listCourse_time_start[3:5])
            d=float(listCourse_time_end[0:2]+"."+listCourse_time_end[3:5])

            timeList1=[]
            for i in np.arange(a,b,.01):
                temp=format(i,'.2f')
                timeList1.append(temp)

            timeList2=[]
            for i in np.arange(c,d,.01):
                temp=format(i,'.2f')
                timeList2.append(temp)
            result=False
            for x in timeList1:
                for y in timeList2:
                    if x==y:
                        result=True
            if result:
                messages.warning(request, "Course has overlap with course added to schedule.")
                # Refresh current page
                return redirect(request.META.get('HTTP_REFERER'))
            
    # Everything is good! Add course to schedule
    else:
        current_schedule.add_course(course)
        messages.success(request, "Course added successfully.")
        return redirect(request.META.get('HTTP_REFERER'))


def delete_course_from_schedule(request, course_number):
    # Delete course if it exists
    current_schedule = request.user.schedule
    course = Course.objects.get(course_number=course_number)

    # If course is in schedule
    if current_schedule.courses.filter(course_number=course_number).exists():
        messages.success(request, "Course successfully deleted.")
        current_schedule.delete_course(course)
        # Refresh current page
        return redirect(request.META.get('HTTP_REFERER'))
    # Course cannot be deleted because it isn't in the schedule
    else:
        messages.warning(request, "Course does not exist.")
        return redirect(request.META.get('HTTP_REFERER'))
