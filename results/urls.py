from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ResultViewSet

app_name = 'results'

# API маршруты
router = DefaultRouter()
router.register(r'results', ResultViewSet, basename='result')

# Визуальные представления
urlpatterns = [
    path('', views.result_list, name='result_list'),
    path('event/<int:event_id>/', views.event_results, name='event_results'),
    path('event/<int:event_id>/add/', views.add_result, name='add_result'),
]

# Подключаем API без "api/"
urlpatterns += router.urls
