from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Comment
from .forms import AddCommentForm


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'comment/add_comment.html'
    #fields='__all__'

    def form_valid(self, form):
        form.instance.course_id=self.kwargs['course_number']
        return super().form_valid(form)


    
