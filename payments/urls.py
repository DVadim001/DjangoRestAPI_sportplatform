from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'payments'

router = DefaultRouter()
router.register(r'api/payments', views.PaymentViewSet, basename='payments')
router.register(r'api/services', views.ServiceTypeViewSet, basename='services')

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/', views.payment_create, name='payment_create'),
    path('api/', include(router.urls)),  # <-- исправлено
]
