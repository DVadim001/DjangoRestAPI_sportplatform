from django.urls import path
from .views import about_view
from . import views

from rest_framework.routers import DefaultRouter
from .api_views import StaticPageViewSet

from django.urls import path, include

app_name = 'pages'

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('faq/', views.faq_view, name='faq'),
]

router = DefaultRouter()
router.register(r'pages', StaticPageViewSet, basename='staticpage')

urlpatterns += [
    path('api/pages/', include('pages.api_urls')),
]