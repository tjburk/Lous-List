from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'list_classes'
urlpatterns = [
    path('update/', views.update_course_db, name="update"),
    path('comment/', include('comment.urls')),
    path('<str:subjects_displayed>/', views.IndexView.as_view(), name="classes"),
    path('description/<int:course_number>/', views.description, name='description'),
]