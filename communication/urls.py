from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/new/', views.message_create, name='message_create'),

    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notifications/<int:pk>/delete/', views.notification_confirm_delete, name='notification_confirm_delete'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),

]
