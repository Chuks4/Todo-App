from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('home/', include('activities.urls')),
    path('notifications/', include('notifications.urls')),
    
    
    # Python social url
    path('auth/', include('social_django.urls', namespace='social')),
    # Password reset Paths
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='confirm_password.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password_complete.html'), name='password_reset_complete')    


]
