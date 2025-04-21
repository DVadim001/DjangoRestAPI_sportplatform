from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'venues'

router = DefaultRouter()
router.register(r'api/venues', views.VenueViewSet, basename='venues')

urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('create/', views.venue_create, name='venue_create'),
    path('<int:pk>/', views.venue_detail, name='venue_detail'),
    path('<int:pk>/edit/', views.venue_edit, name='venue_edit'),
    path('<int:pk>/delete/', views.venue_delete, name='venue_delete'),
    path('', include(router.urls)),
]