from django.shortcuts import render
from django.views.generic import ListView
from list_classes.models import Course
from django.db.models import Q

"""
Title: Django Search Tutorial
Author: Will Vincent
Date: 10/31/2022
URL: https://learndjango.com/tutorials/django-search-tutorial
"""

class SearchResultsView(ListView):
    model = Course
    template_name = 'list_classes/index.html'

    def get_queryset(self):
        search_query = self.request.GET.get("search_query")
        queryset = Course.objects.filter(
            Q(description__icontains=search_query) |
            Q(instructor_name__icontains=search_query) |
            Q(meetings_facility_description__icontains=search_query) |
            Q(secondary_meetings_facility_description__icontains=search_query) |
            Q(secondary_meetings_facility_description__icontains=search_query) |
            Q(meetings_days__icontains=search_query) |
            Q(secondary_meetings_days__icontains=search_query),
        )
        queryset = queryset.order_by('subject', 'catalog_number')
        queryset = queryset.filter(component__in=['LEC', 'IND'])
        return queryset
