from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ScheduleViewSet, CategoryViewSet,
    schedule_list, schedule_create, schedule_delete, schedule_detail, schedule_update
)

app_name = 'schedules'

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', schedule_list, name='schedule_list'),
    path('<int:schedule_id>/', schedule_detail, name='schedule_detail'),
    path('create/', schedule_create, name='schedule_create'),
    path('<int:schedule_id>/update/', schedule_update, name='schedule_update'),
    path('<int:schedule_id>/delete/', schedule_delete, name='schedule_delete'),
]

urlpatterns += router.urls
