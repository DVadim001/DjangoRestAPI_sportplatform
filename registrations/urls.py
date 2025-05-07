from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'registrations'

router = DefaultRouter()
router.register(r'registrations', views.RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('create/', views.register_for_event, name='register_for_event'),
    path('cancel/<int:registration_id>/', views.cancel_registration, name='cancel_registration'),
    path('register/<int:event_id>/', views.register_for_event_specific, name='register_for_event_specific'),
]

# Подключаем API без лишнего "api/"
urlpatterns += router.urls
