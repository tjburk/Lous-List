from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class TestLousList(TestCase):
    def test_home_page_uses_correct_template(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'lous_list/home.html')

#https://mkdev.me/posts/how-to-cover-django-application-with-unit-tests


class TestSignIn(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpass', email='test@testing.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='testpass')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testpass')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)