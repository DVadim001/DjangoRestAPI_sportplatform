from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'clubs'

router = DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'memberships', views.MemberViewSet)

urlpatterns = router.urls + [
    path('', views.club_list, name='club_list'),
    path('create/', views.club_create, name='club_create'),
    path('<int:pk>/', views.club_detail, name='club_detail'),
    path('<int:pk>/edit/', views.club_edit, name='club_edit'),
    path('<int:pk>/delete/', views.club_delete, name='club_delete'),
    path('<int:club_id>/join/', views.join_club, name='join_club'),
]
