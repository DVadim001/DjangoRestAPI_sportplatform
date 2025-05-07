from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StaticPageViewSet

router = DefaultRouter()
router.register(r'static-pages', StaticPageViewSet, basename='static-page')

urlpatterns = [
    path('', include(router.urls)),
]