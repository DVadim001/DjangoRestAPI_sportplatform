from rest_framework import serializers
from .models import Event
from results.models import Result

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'location', 'description']


class ResultSerializer(serializers.ModelSerializer):
    event = serializers.ReadOnlyField(source='event.name')

    class Meta:
        model = Result
        fields = ['id', 'event', 'participant', 'score', 'position']
        depth = 1  # Это позуволит включить подробные данные о связанных объектах, например, об участниках
