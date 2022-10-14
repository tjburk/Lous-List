from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="classes"),
    path('description/<int:course_number>/',views.description,name="description")
]