from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


def index(request):
    return(HttpResponse('Index Page'))

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def numero(request, id):
    result= id + 100 * 2
    return HttpResponse("<h1>El numero es %s</h1>" % result)


def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return(JsonResponse(projects, safe=False))

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return(HttpResponse('tasks: %s' % task.title))