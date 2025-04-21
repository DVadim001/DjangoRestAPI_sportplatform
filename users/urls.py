from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet, basename='userprofile')
router.register(r'settings', views.UserSettingsViewSet, basename='usersettings')

urlpatterns = [
    path('api/', include(router.urls)),

    path('profile/<int:user_id>', views.profile_view, name='profile_view'),
    path('register/', views.register, name='register'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.update_profile_settings, name='update_profile_settings'),
    path('users_list/', views.get_all_users, name='users_list'),
    # path('search/', views.search_user_by_filter, name='search_user'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_request, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
