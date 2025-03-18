from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from base.models import Task

# Create your views here.

# TEST SERVER
# def tasks_list(task):
#     return HttpResponse('Tasks List')

class ListTasks(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'base/task_list.html'

class DetailTask(DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'base/task_detail.html'

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'











