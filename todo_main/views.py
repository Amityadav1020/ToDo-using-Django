from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(isCompleted=False).order_by('-updated_at')  #'-' is used for we get the data in descending order, by defult it is ascending order
    # print(tasks)
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html',context)