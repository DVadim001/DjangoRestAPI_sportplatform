from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageVisitViewSet, UserActionViewSet

router = DefaultRouter()
router.register(r'pagevisits', PageVisitViewSet, basename='pagevisit')
router.register(r'useractions', UserActionViewSet, basename='useraction')

urlpatterns = [
    path('', include(router.urls)),
]
