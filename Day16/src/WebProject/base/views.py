from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from base.models import Task


# Create your views here.

# TEST SERVER
# def tasks_list(task):
#     return HttpResponse('Tasks List')

class ListTasks(ListView):
    model = Task
    context_object_name = 'Tasks'