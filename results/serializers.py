from rest_framework import serializers
from .models import Event, Result


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'location', 'description']


class ResultSerializer(serializers.ModelSerializer):
    event = serializers.ReadOnlyField(source='event.name')  # Показываем имя события, а не ID

    class Meta:
        model = Result
        fields = ['id', 'event', 'participant', 'score', 'position']
        depth = 1

class AdminResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'