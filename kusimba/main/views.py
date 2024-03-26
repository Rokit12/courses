from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def finder(request):
    return render(request, 'course_finder.html')


def details(request):
    return render(request, 'course_details.html')


def earn_certificate(request):
    return render(request, 'earn_certificate.html')


def account(request):
    return render(request, 'account.html')
