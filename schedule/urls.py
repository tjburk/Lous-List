from django.urls import path
from schedule.views import (get_schedule_courses, add_course_to_schedule, delete_course_from_schedule)

app_name = 'schedule'
urlpatterns = [
    path('', get_schedule_courses),
    path('add_course/<course_number>', add_course_to_schedule, name='add_course'),
    path('delete_course/<course_number>', delete_course_from_schedule, name='delete_course'),

]