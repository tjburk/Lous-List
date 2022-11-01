from django.test import TestCase
from list_classes.models import Course


class testcases(TestCase):
    def test_call_view(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)