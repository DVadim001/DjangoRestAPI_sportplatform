from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet

router = DefaultRouter()
router.register(r'registrations', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', include(router.urls)),
]
