from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

# DRF Spectacular schema views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# API endpoints
api_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('pages/', include('pages.api_urls')),
    path('users/', include('users.urls')),
    path('communication/', include('communication.urls')),
    path('clubs/', include('clubs.urls')),
    path('results/', include('results.urls')),
    path('venues/', include('venues.urls')),
    path('payments/', include('payments.urls')),
    path('registrations/', include('registrations.urls')),
    path('events/', include('events.urls')),
    path('equipment/', include('equipment.urls')),
    path('analytics/', include('analytics.urls')),
    path('schedules/', include('schedules.urls')),
]

# HTML-интерфейс
html_urlpatterns = [
    path('', views.main_view, name='main'),
    path('search/', views.global_search, name='global_search'),
    path('info/', include('pages.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('communication/', include('communication.urls')),
    path('clubs/', include('clubs.urls')),
    path('results/', include('results.urls')),
    path('venues/', include('venues.urls')),
    path('payments/', include('payments.urls')),
    path('registrations/', include('registrations.urls')),
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
