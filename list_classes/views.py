from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Course

import requests


def description(request, course_number):
    course = get_object_or_404(Course, pk=course_number)
    # Only display LAB and DIS sections matching same catalog number and subject as lecture
    component_list = Course.objects.filter(component__in=['LAB', 'DIS'],
                                           catalog_number=course.catalog_number,
                                           subject=course.subject)
    return render(request, "list_classes/description.html", {'course': course, 'component_list': component_list})


class IndexView(generic.ListView):
    template_name = 'list_classes/index.html'
    context_object_name = 'course_list'
    subject_filter = []

    def get_queryset(self):
        # Sort data by catalog number/subject and only display LECTURE sections on index page
        self.subject_filter = []
        queryset = Course.objects.order_by('subject', 'catalog_number')
        queryset = queryset.filter(component__in=['LEC', 'IND'])

        # Change subjects displayed based on information from home screen
        # Display all subjects
        if self.kwargs['subjects_displayed'] == "all":
            subject_list = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
            for mnemonic in subject_list:
                mnemonic = mnemonic["subject"]
                self.subject_filter.append(mnemonic)

        # Add particular subject to subject filter dict
        else:
            self.subject_filter.append(self.kwargs['subjects_displayed'])

        # Display all subjects in subject filter dict
        queryset = queryset.filter(subject__in=self.subject_filter)
        return queryset


def update_course_db(request):

    # Add every class to the database
    subject_list = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
    for mnemonic in subject_list:
        mnemonic = mnemonic["subject"]
        print(mnemonic)
        luthers_list = requests.get('http://luthers-list.herokuapp.com/api/dept/' + mnemonic + '/?format=json').json()

        for c in luthers_list:
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
                # Set up default values for meeting
                meetings_days='-',
                meetings_start_time="",
                meetings_end_time="",
                meetings_facility_description='-',
                secondary_meetings_days='-',
                secondary_meetings_start_time="",
                secondary_meetings_end_time="",
                secondary_meetings_facility_description='-',
            )

            # Change Meetings values
            if len(c['meetings']) >= 1: # One or two meeting times
                course.meetings_days=c['meetings'][0]['days']
                course.meetings_start_time=c['meetings'][0]['start_time'][0:5].replace(".", ":")
                course.meetings_end_time=c['meetings'][0]['end_time'][0:5].replace(".", ":")
                course.meetings_facility_description=c['meetings'][0]['facility_description']
            if len(c['meetings']) == 2: # Two meeting times
                course.secondary_meetings_days=c['meetings'][1]['days']
                course.secondary_meetings_start_time=c['meetings'][1]['start_time'][0:5].replace(".", ":")
                course.secondary_meetings_end_time=c['meetings'][1]['end_time'][0:5].replace(".", ":")
                course.secondary_meetings_facility_description=c['meetings'][1]['facility_description']
            course.save()

    return HttpResponseRedirect(reverse('list_classes:classes', args=['all']))
