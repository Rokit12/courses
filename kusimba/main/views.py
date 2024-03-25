from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def finder(request):
    return render(request, 'course_finder.html')
