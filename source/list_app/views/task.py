
from django.shortcuts import render

from list_app.models import Task


def add_task_view(request):
    if request.method =='GET':
        return render(request, 'new_task.html')
    context = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date')
    }
    return render (request, 'task.html', context=context)


def display_task_view(request):
    id = request.GET.get('id')
    task = Task.objects.get(pk=id)
    context = {
        "task": task
    }
    return render(request, 'task.html', context=context)
