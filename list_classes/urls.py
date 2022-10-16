from django.urls import path
from . import views

app_name = 'list_classes'
urlpatterns = [
    path('',views.IndexView.as_view(),name="classes"),
    path('update',views.update_course_db,name="update")
]