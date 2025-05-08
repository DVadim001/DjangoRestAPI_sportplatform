from django.urls import path
from . import views

app_name = 'registrations'

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('create/', views.register_for_event, name='register_for_event'),
    path('cancel/<int:registration_id>/', views.cancel_registration, name='cancel_registration'),
    path('register/<int:event_id>/', views.register_for_event_specific, name='register_for_event_specific'),
]
