from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.result_list, name='result_list'),
    path('event/<int:event_id>/', views.event_results, name='event_results'),
    path('event/<int:event_id>/add/', views.add_result, name='add_result'),
]
