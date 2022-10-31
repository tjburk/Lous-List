from django.shortcuts import render
from django.views.generic import ListView
from list_classes.models import Course


class SearchResultsView(ListView):
    model = Course
    template_name = 'list_classes/index.html'

    def get_queryset(self):  # new
        search_query = self.request.GET.get("search_query")
        object_list = Course.objects.filter(
            # Searches for query based on fields below
            description__icontains=search_query,
        )
        return object_list
