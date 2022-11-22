from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView
from .views import set_up_profile

urlpatterns = [
    path('', TemplateView.as_view(template_name='lous_list/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list_classes/', include('list_classes.urls'), name='list_classes'),
    path('search/', include('search.urls'), name='search'),
    path('friend/', include('friend.urls'), name='friend'),
    path('schedule/', include('schedule.urls'), name='schedule'),
    path('accounts/profile/<user_id>/', set_up_profile, name='profile'),
]
