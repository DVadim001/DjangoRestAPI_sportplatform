from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'results'

router = DefaultRouter()
router.register(r'events', views.EventViewSet, basename='events')
router.register(r'results', views.ResultViewSet, basename='results')

urlpatterns = [
    path('', views.result_list, name='result_list'),
    path('api/', include(router.urls)),
    path('event/<int:event_id>/', views.event_results, name='event_results')
]
