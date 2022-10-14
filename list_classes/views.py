from django.shortcuts import get_object_or_404, render

from .models import Course
import requests
# Create your views here.
def index(request):
    response = requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    return render(request,'list_classes/classes.html',{'response':response})

def description(request, course_number):
    course = get_object_or_404(Course, pk=course_number)
    return render(request, 'list_classes/description.html',{'course':course})
