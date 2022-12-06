from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('<int:course_number>/', views.AddCommentView.as_view(), name='add_comment'),
    path('<int:user_id>/', views.AddCommentView.as_view(), name='add_comment_user'),
]