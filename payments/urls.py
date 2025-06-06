from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'payments'

router = DefaultRouter()
router.register(r'payments', views.PaymentViewSet, basename='payments')
router.register(r'services', views.ServiceTypeViewSet, basename='services')

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/', views.payment_create, name='payment_create'),
]

# Подключаем API без лишнего "api/"
urlpatterns += router.urls
