from django.urls import path
from . import views
from .views import ListTasks

urlpatterns = [
    path('', ListTasks.as_view(), name='tasks'),
]