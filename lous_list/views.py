from django.shortcuts import render
from django.contrib.auth.models import User
from schedule.views import get_schedule_courses


def set_up_profile(request, user_id):
    current_user = request.user

    # All user's friends
    current_user_friend_ids = []
    friend_list_query = current_user.friends.all()
    for friend_list in friend_list_query:
        current_user_friend_ids.append(friend_list.user_id)

    user = User.objects.get(id=user_id)
    courses = get_schedule_courses(request, user_id)
    return render(request, 'account/profile.html', {'current_user': current_user,
                                                    'current_user_friend_ids': current_user_friend_ids,
                                                    'user': user,
                                                    'courses': courses})
