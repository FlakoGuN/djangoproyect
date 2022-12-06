from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def hello(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render (request, 'projects.html', { 'projects': projects})

def tasks(request):
    tasks = Task.objects.all()
    return render (request, 'tasks.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': CreateNewTask()})
    else:
       Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
       return redirect ('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render (request, 'create_project.html', {'form': CreateNewProject()})
    else:
       Project.objects.create(name=request.POST["name"])
       
    return redirect ('/projects/')