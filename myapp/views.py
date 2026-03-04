from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def numero(request, id):
    result= id + 100 * 2
    return HttpResponse("<h1>El numero es %s</h1>" % result)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')
    

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    return render(request, 'task.html')

# def projects(request):
#     projects = list(Project.objects.values())
#     return(JsonResponse(projects, safe=False))

# def tasks(request, id):
#     task = get_object_or_404(Task, id=id)
#     return(HttpResponse('tasks: %s' % task.title))