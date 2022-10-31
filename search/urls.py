from django.urls import path
from .views import SearchResultsView

"""
Title: Django Search Tutorial
Author: Will Vincent
Date: 10/31/2022
URL: https://learndjango.com/tutorials/django-search-tutorial
"""

app_name = 'search'
urlpatterns = [
    path("", SearchResultsView.as_view(), name="search"),
]