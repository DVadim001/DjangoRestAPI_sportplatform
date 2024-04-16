from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_number',
                  'birth_date',
                  'gender',
                  'height',
                  'weight',
                  'experience_level',
                  'preferred_sports',
                  'medical_information',
                  'equipment',
                  'club_memberships',
                  'subscriptions',
                  'user']


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['receive_newsletters', 'public_profile']
