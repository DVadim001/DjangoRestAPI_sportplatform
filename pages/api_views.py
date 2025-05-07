from rest_framework import viewsets
from .models import StaticPage
from .serializers import StaticPageSerializer

class StaticPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer