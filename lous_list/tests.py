from django.test import TestCase


class TestLousList(TestCase):
    def test_home_page_uses_correct_template(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'lous_list/home.html')