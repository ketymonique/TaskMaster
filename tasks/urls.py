from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Define a URL padrão para listar as tarefas
]
