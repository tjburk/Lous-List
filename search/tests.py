from django.test import TestCase
from list_classes.models import Course


import json

from django.test import TestCase
from django.test.client import RequestFactory

from list_classes.models import Course


class TestSearch(TestCase):
    def setUpTestData(self):
        # Create 10 courses
        number_of_courses = 10

        for course_index in range(number_of_courses):
            Course.objects.create(
                course_number=12345 + course_index,
                description=f'Test Course {course_index}',
            )

    def test_search_url_exists_at_desired_location(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_search_uses_correct_template(self):
        response = self.client.get('/search/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/index.html')

