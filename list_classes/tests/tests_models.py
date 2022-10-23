from django.test import TestCase

from list_classes.models import Course


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(course_number=12345, description='Introduction to Testing Courses', instructor_name='Test Case')

    def test_course_number_label(self):
        course = Course.objects.get(course_number=12345)
        course_number_label = course._meta.get_field('course_number').verbose_name
        self.assertEqual(course_number_label, 'course number')

    def test_description_label(self):
        course = Course.objects.get(course_number=12345)
        description_label = course._meta.get_field('description').verbose_name
        self.assertEqual(description_label, 'description')

    def test_instructor_name_max_length(self):
        course = Course.objects.get(course_number=12345)
        max_length = course._meta.get_field('instructor_name').max_length
        self.assertEqual(max_length, 50)

    def test_enrollment_total_greater_or_equal_enrollment_available(self):
        course = Course.objects.get(course_number=12345)
        enrollment = {course.enrollment_total} >= {course.enrollment_available}
        self.assertEqual(enrollment, True)

