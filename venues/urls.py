from django.urls import path
from . import views

app_name = 'venues'

urlpatterns = [
    path('', views.venue_list, name='venue_list'),
    path('create/', views.venue_create, name='venue_create'),
    path('<int:pk>/', views.venue_detail, name='venue_detail'),
    path('<int:pk>/edit/', views.venue_edit, name='venue_edit'),
    path('<int:pk>/delete/', views.venue_delete, name='venue_delete'),
]
