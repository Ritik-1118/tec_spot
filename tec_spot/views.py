from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def feature(request):
    return render(request, 'feature.html')


def quote(request):
    return render(request, 'quote.html')


def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')

