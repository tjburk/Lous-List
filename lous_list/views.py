from django.shortcuts import render
from django.contrib.auth.models import User
from schedule.views import get_schedule_courses


def set_up_profile(request, user_id):
    user = User.objects.get(id=user_id)
    schedule_courses = get_schedule_courses(request)
    return render(request, 'account/profile.html', {'user': user, 'courses': schedule_courses})
