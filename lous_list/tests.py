from django.test import TestCase


class home_page_uses_correct_template(TestCase):
    def test_call_view(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'lous_list/home.html')