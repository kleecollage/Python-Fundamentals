from django.http.response import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from base.models import Task

# Create your views here.
# TEST SERVER
# def tasks_list(task):
#     return HttpResponse('Tasks List')

class Login(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class ListTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'base/task_list.html'
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['Tasks'] = context['Tasks'].filter(user=self.request.user)
        context['count'] = context['Tasks'].filter(completed=False).count()

        query = self.request.GET.get('search-area') or ''
        if query:
            context['Tasks'] = context['Tasks'].filter(title__icontains=query)
        context['query'] = query
        return context

class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'Task'
    template_name = 'base/task_detail.html'
    # Verify if user have permission to see the object
    def dispatch(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            if obj.user != self.request.user:
                return redirect('tasks')
        except Http404:
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
    # Filter by task that belongs to the logged user
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = '__all__'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'












