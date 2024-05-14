from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('read-notifications/<str:pk>', views.read_notifications, name='read-notification'),
]


   