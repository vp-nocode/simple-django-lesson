# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>This is my first Django project!</h1>")

def new(request):
    return HttpResponse("<h1>This is second page of my Django project!</h1>")