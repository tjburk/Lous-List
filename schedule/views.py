from django.shortcuts import render, redirect
from list_classes.models import Course
from django.contrib import messages
from schedule.models import Schedule


def get_schedule_courses(request):
    # If schedule doesn't exist, create one
    try:
        Schedule.objects.get(user=request.user)
    except Schedule.DoesNotExist:
        Schedule.objects.create(user=request.user)

    # All user's courses in schedule
    schedule_courses = []
    course_list_query = request.user.schedule.courses.all()
    for course_list in course_list_query:
        course = Course.objects.get(course_number=course_list.course_number)
        schedule_courses.append(course)

    return schedule_courses


def add_course_to_schedule(request, course_number):
    # Add course if it doesn't already exist
    current_schedule = request.user.schedule

    # If course is already in schedule
    if current_schedule.courses.filter(course_number=course_number).exists():
        messages.warning(request, "Course already in schedule.")
        # Refresh current page
        return redirect(request.META.get('HTTP_REFERER'))
    # If course times overlap

    # Everything is good! Add course to schedule
    else:
        current_schedule.add_course(course_number)
        messages.success(request, "Course added successfully.")
        return redirect(request.META.get('HTTP_REFERER'))


def delete_course_from_schedule(request, course_number):
    # Delete course if it exists
    current_schedule = request.user.schedule

    # If course is in schedule
    if current_schedule.courses.filter(course_number=course_number).exists():
        messages.success(request, "Course successfully deleted.")
        current_schedule.delete_course(course_number)
        # Refresh current page
        return redirect(request.META.get('HTTP_REFERER'))
    # Course cannot be deleted because it isn't in the schedule
    else:
        messages.warning(request, "Course does not exist.")
        return redirect(request.META.get('HTTP_REFERER'))
