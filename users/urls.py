from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginUser, name='login'),
    path('register/', views.createUser, name='register'),
    path('logout/', views.logoutUser, name='logout-user'),
    path('user-account/', views.userAccount, name='user-account'),
    path('update-user-profile/', views.updateUserProfile, name='update-profile'),
    path('delete-user/', views.deleteUser, name='delete-user'),

]