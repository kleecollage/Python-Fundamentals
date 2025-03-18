from django.urls import path
from . import views
from .views import ListTasks, DetailTask, CreateTask

urlpatterns = [
    path('', ListTasks.as_view(), name='tasks'),
    path('task/<int:pk>', DetailTask.as_view(), name='details'),
    path('create-task/', CreateTask.as_view(), name='create'),
]