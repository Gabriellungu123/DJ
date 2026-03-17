from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask


def index(request):
    title= 'Django Course'
    return render(request, 'index.html',{
        'titulo': title
    })

def about(request):
    username = 'Gabriel'
    return render(request, 'about.html',{
        'usuario' : username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def numero(request, id):
    result= id + 100 * 2
    return HttpResponse("<h1>El numero es %s</h1>" % result)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'proyectos': projects
    })
    

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    return render(request, 'task.html',{
        'tareas':task
    })

# def projects(request):
#     projects = list(Project.objects.values())
#     return(JsonResponse(projects, safe=False))

# def tasks(request, id):
#     task = get_object_or_404(Task, id=id)
#     return(HttpResponse('tasks: %s' % task.title))

def create_task(request):
    if request.method == 'GET':
        #Show interface
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description= request.POST['description'], project_id=2)
        return redirect('/tasks/')
        