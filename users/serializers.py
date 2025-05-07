from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserSettings

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
            'receive_newsletters', 'public_profile'
        ]

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['receive_newsletters', 'public_profile', 'privacy_settings']

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_staff', 'is_superuser', 'is_active', 'date_joined'
        ]

class AdminUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserProfile
        fields = '__all__'
