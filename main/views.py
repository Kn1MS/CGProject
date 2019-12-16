from django.shortcuts import render, redirect
from .models import NumberGenerateTask
from .serializer import Serializer
import subprocess

# Create your views here.

def MainView(request):
    GenerateTasks = Task.objects.filter(status="Solved").order_by('-id')
    TasksSerializer = TaskSerializer(GenerateTasks, many=True)
    return render(request, "main/index.html", {"GenerateTasks": GenerateTasks.data})

def CreateTask(request):
    NumberGenerateTask = NumberGenerateTask()
    NumberGenerateTask.save()
    GenerateNumbers()
    return redirect('/')

def GenerateNumbers():
	subprocess.Popen("bash main/ToAzure.sh", shell = True)