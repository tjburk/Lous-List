from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Comment


# Create your views here.
class AddCommentView(CreateView):
    model = Comment
    template_name = 'comment/add_comment.html'
    fields='__all__'
