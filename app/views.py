from django.shortcuts import render

def main(request):
    return render(request, 'app/main.html')

def login(request):
    return render(request, 'app/main.html')
