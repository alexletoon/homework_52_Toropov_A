from django.shortcuts import render


def add_task_view(request):
    if request.method =='GET':
        return render(request, 'new_task.html')
    return render (request, 'index.html')