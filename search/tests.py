
from django.test import TestCase
from django.test import Client
from list_classes.models import Course
from django.shortcuts import get_object_or_404


class TestSearch(TestCase):
    def setUp(self):
        self.client = Client()
        Course.objects.create(description="Software Testing", course_number=16617)

    def test_search_for_word_doesnt_crash(self):
        response = self.client.get('/search/', {'search_query': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_search_redirects_to_index_page(self):
        response = self.client.get('/search/', {'search_query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/index.html')

    def test_search_doesnt_bring_up_results(self):
        response = self.client.get('/search/', {'search_query': 'dfadsjiofhsjakjfsk'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No classes are available.")
