from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number',
                  'birth_date',
                  'gender', 'height',
                  'weight',
                  'experience_level',
                  'preferred_sports',
                  'medical_information',
                  'equipment',
                  'club_memberships',
                  'subscriptions',
                  'privacy_settings']


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['receive_newsletters', 'public_profile']
