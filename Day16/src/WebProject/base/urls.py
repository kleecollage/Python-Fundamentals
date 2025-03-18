from django.urls import path
from . import views
from .views import ListTasks, DetailTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', ListTasks.as_view(), name='tasks'),
    path('task/<int:pk>', DetailTask.as_view(), name='details'),
    path('create-task/', CreateTask.as_view(), name='create'),
    path('update-task/<int:pk>', UpdateTask.as_view(), name='update'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete'),
]