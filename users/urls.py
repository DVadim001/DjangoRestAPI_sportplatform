from django.urls import path
from .views import profile_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
