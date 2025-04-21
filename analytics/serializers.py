from rest_framework import serializers
from .models import PageVisit, UserAction


class PageVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageVisit
        fields = ['id', 'user', 'page_url', 'timestamp']


class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ['id', 'user', 'action_type', 'timestamp', 'additional_info']
