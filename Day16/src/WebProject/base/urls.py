from django.urls import path
from . import views
from .views import ListTasks, DetailTask, CreateTask, UpdateTask, DeleteTask, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ListTasks.as_view(), name='tasks'),
    path('task/<int:pk>', DetailTask.as_view(), name='details'),
    path('create-task/', CreateTask.as_view(), name='create'),
    path('update-task/<int:pk>', UpdateTask.as_view(), name='update'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete'),
]