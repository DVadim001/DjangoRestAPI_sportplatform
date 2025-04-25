from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserSettings
from django.forms import DateInput, Textarea
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField
from clubs.models import Club


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)  # ← ДОБАВЬ ЭТО ПОЛЕ

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={
        'placeholder': '+1234567890'
    }), label='Номер телефона')

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
            'club_memberships',
            'subscriptions'
        ]
        widgets = {
            'club_memberships': forms.CheckboxSelectMultiple(),
            'subscriptions': forms.CheckboxSelectMultiple(),
            'birth_date': DateInput(attrs={
                'type': 'date',
                'max': timezone.now().date().isoformat()
            }),
            'bio': Textarea(attrs={'placeholder': 'Расскажите о себе...'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club_memberships'].queryset = Club.objects.all()
        if self.instance and self.instance.user:
            self.fields['subscriptions'].queryset = User.objects.exclude(id=self.instance.user.id)


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['receive_newsletters', 'public_profile']


class UserInfoForm(forms.ModelForm):
    """Отдельная форма для редактирования first_name, last_name и email пользователя."""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
