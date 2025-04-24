from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserSettings  # добавили импорт UserSettings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'birth_date', 'gender', 'height', 'weight',
            'experience_level', 'preferred_sports', 'medical_information',
            'equipment', 'club_memberships', 'subscriptions', 'user',
            'receive_newsletters', 'public_profile'  # можно добавить, если нужно
        ]

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['receive_newsletters', 'public_profile', 'privacy_settings']
