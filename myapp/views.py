from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return(HttpResponse('Index Page'))

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def numero(request, id):
    result= id + 100 * 2
    return HttpResponse("<h1>El numero es %s</h1>" % result)


def about(request):
    return HttpResponse("About")

