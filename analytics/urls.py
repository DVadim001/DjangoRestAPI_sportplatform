from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageVisitViewSet, UserActionViewSet, page_visits_chart, user_actions_chart
from django.shortcuts import render

router = DefaultRouter()
router.register(r'pagevisits', PageVisitViewSet)
router.register(r'useractions', UserActionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('page_visits/', page_visits_chart, name='page_visits_chart'),
    path('user_actions/', user_actions_chart, name='user_actions_chart'),
    path('', lambda request: render(request, 'analytics/analytics_home.html'), name='analytics_home'),
]
