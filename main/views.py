from django.shortcuts import render, redirect
from .models import NumberGenerateTask
from .serializer import Serializer
import subprocess

# Create your views here.

def MainView(request):
    GenerateTasks = NumberGenerateTask.objects.filter(status="Done").order_by('-id')
    TasksSerializer = Serializer(GenerateTasks, many=True)
    return render(request, "main/index.html", {"GenerateTasks": TasksSerializer.data})

def CreateTask(request):
    GenerateTask = NumberGenerateTask()
    GenerateTask.save()
    GenerateNumbers()
    return redirect('/')

def GenerateNumbers():
	subprocess.Popen("bash main/ToAzure.sh", shell = True)