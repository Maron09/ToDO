from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *



def addTask(request):
    task = request.POST['Task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)  #this fetches the data from database if it exists or gives 404
    task.is_complete = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = False
    task.save()
    return redirect('home')


def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['Task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context ={
            "get_task":get_task
        }
        return render(request, 'edit.html', context)


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')