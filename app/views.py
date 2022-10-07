from django.shortcuts import render

def main(request):
    return render(request, 'app/main.html')