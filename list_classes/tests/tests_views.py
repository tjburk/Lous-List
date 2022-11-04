from django.test import TestCase
from django.urls import reverse

from list_classes.models import Course
from comment.models import Comment


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 courses
        number_of_courses = 10

        for course_index in range(number_of_courses):
            Course.objects.create(
                course_number=12345 + course_index,
                description=f'Test Course {course_index}',
                component='LEC',
                subject='CS'
            )

        # Create a comment on course 12345
        Comment.objects.create(course=Course.objects.get(course_number=12345), name="Test Comment")


    ### Test Index View ###

    def test_index_url_exists_at_desired_location(self):
        response = self.client.get('/list_classes/all/')
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        response = self.client.get('/list_classes/all/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/index.html')

    def test_index_display_multiple_classes(self):
        response = self.client.get('/list_classes/CS/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [Course.objects.get(course_number=12345),
                                                                   Course.objects.get(course_number=12346),
                                                                   Course.objects.get(course_number=12347),
                                                                   Course.objects.get(course_number=12348),
                                                                   Course.objects.get(course_number=12349),
                                                                   Course.objects.get(course_number=12350),
                                                                   Course.objects.get(course_number=12351),
                                                                   Course.objects.get(course_number=12352),
                                                                   Course.objects.get(course_number=12353),
                                                                   Course.objects.get(course_number=12354)])


    ### Test Description View ###

    def test_description_url_exists_at_desired_location(self):
        response = self.client.get('/list_classes/description/12345/')
        self.assertEqual(response.status_code, 200)

    def test_description_uses_correct_template(self):
        response = self.client.get('/list_classes/description/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_classes/description.html')


