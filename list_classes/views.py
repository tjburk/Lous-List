from django.shortcuts import render

import requests
# Create your views here.
def index(request):
    response=requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()
    return render(request,'list_classes/classes.html',{'response':response})
