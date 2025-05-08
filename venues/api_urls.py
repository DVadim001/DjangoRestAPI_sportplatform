from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet, basename='venues')

urlpatterns = [
    path('', include(router.urls)),
]
