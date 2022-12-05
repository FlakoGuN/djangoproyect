from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

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