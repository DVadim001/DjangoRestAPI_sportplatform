from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

# DRF Spectacular schema views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# API endpoints — подключаем только api_urls от каждого приложения
api_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('pages/', include('pages.api_urls')),
    path('users/', include('users.api_urls')),
    path('communication/', include('communication.api_urls')),
    path('clubs/', include('clubs.api_urls')),
    path('results/', include('results.api_urls')),
    path('venues/', include('venues.api_urls')),
    path('payments/', include('payments.api_urls')),
    path('registrations/', include('registrations.api_urls')),
    path('events/', include('events.api_urls')),
    path('equipment/', include('equipment.api_urls')),
    path('analytics/', include('analytics.api_urls')),
    path('schedules/', include('schedules.api_urls')),
]

# HTML-интерфейс — только для отображения страниц
html_urlpatterns = [
    path('', views.main_view, name='main'),
    path('search/', views.global_search, name='global_search'),

    path('info/', include('pages.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('communication/', include(('communication.urls', 'communication'), namespace='communication')),
    path('clubs/', include(('clubs.urls', 'clubs'), namespace='clubs')),
    path('results/', include(('results.urls', 'results'), namespace='results')),
    path('venues/', include(('venues.urls', 'venues'), namespace='venues')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
    path('registrations/', include(('registrations.urls', 'registrations'), namespace='registrations')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('equipment/', include(('equipment.urls', 'equipment'), namespace='equipment')),
    path('analytics/', include(('analytics.urls', 'analytics'), namespace='analytics')),
    path('schedules/', include(('schedules.urls', 'schedules'), namespace='schedules')),
]

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include(api_urlpatterns)),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    *html_urlpatterns,
    prefix_default_language=False,
)

# Медиафайлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
