from django.shortcuts import render
from my_site.tasks.models import Task


# Create your views here.


def index(request):
    tasks_list = Task.objects.all()
    context = {"tasks_list": tasks_list}

    return render(request, 'tasks/index.html',  context=context)
