from django.urls import path
from . import views


app_name = 'schedules'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('<int:schedule_id/>', views.schedule_detail, name='schedule_detail'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('<int:schedule_id>/update/', views.schedule_update, name='schedule_update'),
    path('<int:schedule_id>/delete/', views.schedule_delete, name='schedule_delete'),
]

