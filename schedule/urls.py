from django.urls import path
from schedule.views import (add_course_to_schedule, delete_course_from_schedule)

app_name = 'schedule'
urlpatterns = [
    path('add_course/<course_number>', add_course_to_schedule, name='add_course'),
    path('delete_course/<course_number>', delete_course_from_schedule, name='delete_course'),

]