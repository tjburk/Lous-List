from django.test import TestCase
from django.urls import reverse

from comment.models import Comment, Course


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(
            course_number=12345,
            description=f'Test Course',
        )

        # Create a comment on course 12345
        Comment.objects.create(course=Course.objects.get(course_number=12345), name="Test Comment")


    ### Test Comment View ###

    def test_comment_url_exists_at_desired_location(self):
        response = self.client.get('/list_classes/description/12345/comment/')
        self.assertEqual(response.status_code, 200)

    def test_comment_uses_correct_template(self):
        response = self.client.get('/list_classes/description/12345/comment/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/add_comment.html')

