from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('description/<int:course_number>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]