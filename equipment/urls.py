from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'reservations', views.EquipmentReservationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.equipment_list, name='equipment_list'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('create/', views.equipment_create, name='equipment_create'),
    path('<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
    path('<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),
    path('<int:pk>/reserve/', views.equipment_reserve, name='equipment_reserve'),
]
