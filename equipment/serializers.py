from rest_framework import serializers
from .models import Equipment, EquipmentReservation

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class EquipmentReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentReservation
        fields = ['id', 'equipment', 'user', 'event', 'start_date', 'end_date', 'created_at']

class AdminEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
