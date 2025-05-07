from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class PaymentAdminViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AdminOnly]
