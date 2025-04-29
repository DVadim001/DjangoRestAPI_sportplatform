from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('users/', include('users.urls',  namespace='users')),
    path('', views.main_view, name='main'),  # URL для главной страницы
    path('search/', views.global_search, name='global_search'),
    path('communication/', include('communication.urls')),
    path('clubs/', include('clubs.urls')),
    path('results/', include('results.urls')),
    path('venues/', include('venues.urls')),
    path('payments/', include('payments.urls')),
    path('registrations/', include('registrations.urls')),
    path('events/', include('events.urls', namespace='events')),
    path('equipment/', include('equipment.urls', namespace='equipment')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('schedules/', include('schedules.urls', namespace='schedules')),

    prefix_default_language=False,

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
