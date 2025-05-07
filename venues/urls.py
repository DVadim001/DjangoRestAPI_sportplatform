from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'venues'

router = DefaultRouter()
router.register(r'', views.VenueViewSet, basename='venues')  # убираем "venues"

# HTML маршруты
html_urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('create/', views.venue_create, name='venue_create'),
    path('<int:pk>/', views.venue_detail, name='venue_detail'),
    path('<int:pk>/edit/', views.venue_edit, name='venue_edit'),
    path('<int:pk>/delete/', views.venue_delete, name='venue_delete'),
]

# API маршруты
api_urlpatterns = [
    path('', include(router.urls)),  # → /api/venues/
]

urlpatterns = html_urlpatterns + [path('api/', include(api_urlpatterns))]
