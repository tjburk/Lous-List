from django.urls import path
from . import views

app_name = 'list_classes'
urlpatterns = [
    path('<str:subjects_displayed>/',views.IndexView.as_view(),name="classes"),
    path('description/<int:course_number>/', views.description, name='description'),
    path('description/<int:course_number>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('update/',views.update_course_db,name="update"),
]