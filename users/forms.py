from django import forms
from .models import UserProfile
from django.forms import ModelForm


class UserProfileForm(forms.ModelForm):
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


class UserSettingsForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['receive_newsletters', 'public_profile']
