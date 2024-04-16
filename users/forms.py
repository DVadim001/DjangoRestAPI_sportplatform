from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'phone',
                  'email',
                  'password1',
                  'password2']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'birth_date',
            'gender',
            'height',
            'weight',
            'experience_level',
            'preferred_sports',
            'medical_information',
            'equipment',
            'club_memberships',
            'subscriptions'
        ]


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['receive_newsletters', 'public_profile']
