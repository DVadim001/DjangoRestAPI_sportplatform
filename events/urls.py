from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import EventViewSet

app_name = 'events'

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls + [
    path('new/', views.create_new_event, name='create_new_event'),
    path('', views.events_list, name='events_list'),
    path('category/', views.category_list, name='category_list'),
    path('<int:event_id>/', views.event_details, name='event_details'),
    path('<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
]
