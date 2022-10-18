from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Course

import requests

def description(request, course_number):
    course = get_object_or_404(Course, pk=course_number)
    return render(request, 'list_classes/description.html', {'course': course})

class IndexView(generic.ListView):
    template_name = 'list_classes/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()

def update_course_db(request):
    json = requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    
    for c in json:
        course = Course(
            instructor_name = c['instructor']['name'],
            instructor_email = c['instructor']['email'],
            course_number = c['course_number'],
            semester_code = c['semester_code'],
            subject = c['subject'],
            catalog_number = c['catalog_number'],
            description = c['description'],
            units = c['units'],
            component = c['component'],
            class_capacity = c['class_capacity'],
            wait_list = c['wait_list'],
            wait_cap = c['wait_cap'],
            enrollment_total = c['enrollment_total'],
            enrollment_available = c['enrollment_available'],
            topic = c['topic'],
            meetings_days = c['meetings'][0]['days'],
            meetings_start_time = c['meetings'][0]['start_time'],
            meetings_end_time = c['meetings'][0]['end_time'],
            meetings_facility_description = c['meetings'][0]['facility_description'],
        )
        course.save()

    return HttpResponseRedirect(reverse('list_classes:classes'))
