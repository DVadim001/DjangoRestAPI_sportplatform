from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import StaticPageViewSet

app_name = 'pages'

# Основные страницы
urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('faq/', views.faq_view, name='faq'),
]

# API роутер
router = DefaultRouter()
router.register(r'static-pages', StaticPageViewSet, basename='staticpage')

# Добавляем API-роуты напрямую без дополнительного 'api/'
urlpatterns += router.urls
