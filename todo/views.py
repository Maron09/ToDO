from django.shortcuts import render
from base.models import Task




def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')
    context = {'tasks': tasks}
    return render(request, 'home.html', context)