from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tasks_list(task):
    return HttpResponse('Tasks List')