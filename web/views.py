from django.shortcuts import render, HttpResponse

# Create your views here.


def Home(request):
    return HttpResponse("Hello, Home Page")


def About(request):
    return HttpResponse("Hello, About Page")


def Contact(request):
    return HttpResponse("Hello, Contact Page")
