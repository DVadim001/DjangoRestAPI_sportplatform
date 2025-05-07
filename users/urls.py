from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter
from .views_api import CurrentUserView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

# DRF router
router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet, basename='userprofile')

# HTML маршруты
html_urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.user_settings_view, name='user_settings'),
    path('permission_denied/', views.permission_denied_view, name='permission_denied'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='users/change_password.html',
        success_url=reverse_lazy('users:login')
    ), name='change_password'),
]

# API маршруты
api_urlpatterns = [
    path('', include(router.urls)),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = html_urlpatterns + [path('api/', include(api_urlpatterns))]
