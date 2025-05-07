from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from users.serializers import UserSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminOnly]
