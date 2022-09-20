import re
from django.shortcuts import render


def add_task_view(request):
    if request.method =='GET':
        return render(request, 'new_task.html')
    context = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date')
    }
    return render (request, 'task.html', context=context)


# def display_task(request):
