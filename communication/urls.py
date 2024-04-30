from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MessgeViewSet, NotificationViewSet

app_name = 'communication'

router = DefaultRouter()
router.register(r'messages', MessgeViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('messages/', views.message_list, name='message_list'),
    path('messages/create/', views.message_create, name='message_create'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('messages/<int:message_id>/update/', views.message_update, name='message_update'),
    path('messages/<int:message_id>/delete/', views.message_delete, name='message_delete'),
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/<int:notification_id>/delete/', views.notification_delete, name='notification_delete'),
]
