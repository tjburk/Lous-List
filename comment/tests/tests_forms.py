from django.test import TestCase

from list_classes.models import Course
from comment.models import Comment
from comment.forms import AddCommentForm
from django.urls import reverse

class CommentFormTest(TestCase):
    def test_is_valid(self):
        form=AddCommentForm(data={"name": "Test Comment Name", "body": "Test Comment Body"})
        self.assertTrue(form.is_valid())
    
    def name_is_invalid(self):
        form=AddCommentForm(data={"name": "", "body": "Test Comment Body"})
        self.assertFalse(form.is_valid())

    def body_is_invalid(self):
        form=AddCommentForm(data={"name": "Test Comment Name", "body": ""})
        self.assertFalse(form.is_valid())