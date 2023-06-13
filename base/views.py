from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



def addTask(request):
    task = request.POST['Task']
    Task.objects.create(task=task)
    return redirect('home')
