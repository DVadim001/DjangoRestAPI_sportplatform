from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.i18n import i18n_patterns

# DRF Spectacular schema views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # DRF Spectacular (для API-документации)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # API endpoints
    path('api/users/', include('users.urls')),
    path('api/communication/', include('communication.urls')),
    path('api/clubs/', include('clubs.urls')),
    path('api/results/', include('results.urls')),
    path('api/venues/', include('venues.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/registrations/', include('registrations.urls')),
    path('api/events/', include('events.urls')),
    path('api/equipment/', include('equipment.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/schedules/', include('schedules.urls')),
]

urlpatterns += i18n_patterns(
    # Админка и основное
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('search/', views.global_search, name='global_search'),

    # HTML-интерфейс
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
    path('api/users/', include('users.urls')),

    prefix_default_language=False,
)

# Медиафайлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
