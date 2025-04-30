from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'clubs'


router = DefaultRouter()
router.register(f'clubs', views.ClubViewSet)
router.register(f'memberships', views.MemberViewSet)


urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('api/', include(router.urls)),
    path('create/', views.club_create, name='club_create'),
    path('<int:pk>/', views.club_detail, name='club_detail'),
    path('<int:pk>/edit/', views.club_edit, name='club_edit'),
    path('<int:pk>/delete/', views.club_delete, name='club_delete'),
    path('<int:club_id>/join/', views.join_club, name='join_club'),
]
