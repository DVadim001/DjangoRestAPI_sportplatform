from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageVisitViewSet, UserActionViewSet

router = DefaultRouter()
router.register(r'pagevisits', PageVisitViewSet)
router.register(r'useractions', UserActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
