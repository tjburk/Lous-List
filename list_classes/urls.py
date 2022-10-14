from django.urls import path
from . import views

app_name = 'list_classes'
urlpatterns = [
    path('',views.index,name="classes"),
    path('update',views.update_course_db,name="update")
]