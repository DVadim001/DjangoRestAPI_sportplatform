from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.forms import DateInput, Textarea
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField
from clubs.models import Club


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
    avatar = forms.ImageField(required=False)
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={
        'placeholder': '+1234567890'
    }), label='Phone number')

    class Meta:
        model = UserProfile
        fields = [
            'avatar',
            'phone_number',
            'birth_date',
            'bio',
            'gender',
            'height',
            'weight',
            'experience_level',
            'preferred_sports',
            'medical_information',
            'equipment',
            'subscriptions'
        ]
        widgets = {
            'club_memberships': forms.CheckboxSelectMultiple(),
            'birth_date': DateInput(attrs={
                'type': 'date',
                'max': timezone.now().date().isoformat()
            }),
            'bio': Textarea(attrs={'placeholder': 'Расскажите о себе...'}),
            'subscriptions': forms.CheckboxSelectMultiple
        }

        def __init__(self, *args, **kwargs):
            super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
            self.fields['club_membership'].queryset = Club.objects.all()
            if self.instance:
                self.fields['subscriptions'].queryset = User.objects.all().exclude(id=self.instance.user.id)


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['receive_newsletters', 'public_profile']
