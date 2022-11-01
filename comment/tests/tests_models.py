from django.test import TestCase

from list_classes.models import Course
from comment.models import Comment
from django.urls import reverse

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(course_number=12345,
                              description='Introduction to Testing Courses',
                              instructor_name='Test Case',
                              enrollment_available=99,
                              enrollment_total=100)
        Comment.objects.create(course=Course.objects.get(course_number=12345),
                               name="Test Comment")


    ### Test Comment Model ###

    def test_comment_course_label(self):
        comment = Comment.objects.get(name="Test Comment")
        course_label = comment._meta.get_field('course').verbose_name
        self.assertEqual(course_label, 'course')

    def test_comment_name_label(self):
        comment = Comment.objects.get(name="Test Comment")
        name_label = comment._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_comment_name_max_length(self):
        comment = Comment.objects.get(name="Test Comment")
        max_length = comment._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_comment_str_is_comment_format(self):
        comment = Comment.objects.get(name="Test Comment")
        self.assertEqual(str(comment), '"%s" by %s - %s' % (comment.course.description,
                                                            comment.course.instructor_name,
                                                            comment.name))

    def test_comment_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(comment.get_absolute_url(), '/list_classes/description/12345/')

