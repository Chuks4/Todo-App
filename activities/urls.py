from django.urls import path
from . import views



urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('create-task', views.createTask, name='create-task'),
    path('update-task/<str:pk>', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>', views.deleteTask, name='delete-task'),
    path('tasks/', views.tasks, name='tasks'),
    path('task-completed/', views.complete_task, name='task-completed')
]