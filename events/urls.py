from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('new/', views.create_new_event, name='create_new_event'),
    path('', views.events_list, name='events_list'),
    path('category/', views.category_list, name='category_list'),
    # path('search/', views.search_event, name='search_event'),
    path('<int:event_id>/', views.event_details, name='event_details'),
    path('<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event')
]
