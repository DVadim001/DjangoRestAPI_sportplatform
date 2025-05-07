from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'communication'

router = DefaultRouter()
router.register(r'messages', views.MessageViewSet, basename='message')
router.register(r'notifications', views.NotificationViewSet, basename='notification')

urlpatterns = router.urls + [
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/new/', views.message_create, name='message_create'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),

    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notifications/<int:pk>/delete/', views.notification_confirm_delete, name='notification_confirm_delete'),
]
