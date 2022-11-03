
from django.test import TestCase


class TestSearch(TestCase):

    def test_search_url_exists_at_desired_location(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_search_uses_correct_template(self):
        response = self.client.get('/search/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/index.html')

