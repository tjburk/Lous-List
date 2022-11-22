from django.shortcuts import render
from django.contrib.auth.models import User
from schedule.views import get_schedule_courses


def set_up_profile(request, user_id):
    current_user = request.user
    user = User.objects.get(id=user_id)
    courses = get_schedule_courses(request, user_id)
    return render(request, 'account/profile.html', {'current_user': current_user, 'user': user, 'courses': courses})
