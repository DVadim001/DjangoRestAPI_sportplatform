from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import UserProfile, UserSettings
from .forms import CustomUserCreationForm, UserProfileForm, UserSettingsForm
from .serializers import UserProfileSerializer

from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny


def users_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            UserSettings.objects.create(user=user)
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = getattr(user, 'profile', None)
    return render(request, 'users/profile.html', {
        'profile_user': user,
        'profile': profile
    })


@login_required
def edit_profile(request):
    user = request.user

    # Создание профиля, если его нет
    if not hasattr(user, 'profile'):
        UserProfile.objects.create(user=user)

    profile = user.profile

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        # Обновляем данные пользователя (имя и фамилия)
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()

        if profile_form.is_valid():
            profile_form.save()
            user.save()  # сохраняем имя и фамилию
            return redirect('users:profile_view', user_id=user.id)

    else:
        profile_form = UserProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
        'user': user,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(current_password):
            messages.error(request, _('Текущий пароль неверен.'))
        elif new_password != confirm_password:
            messages.error(request, _('Пароли не совпадают.'))
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, _('Пароль успешно изменён.'))
            return redirect('users:profile_view', user_id=request.user.id)

    return render(request, 'users/change_password.html')


@login_required
def user_settings_view(request):
    settings, _ = UserSettings.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, _('Настройки сохранены.'))
            return redirect('users:user_settings')
    else:
        form = UserSettingsForm(instance=settings)
    return render(request, 'users/settings.html', {'form': form})


def permission_denied_view(request):
    return render(request, 'users/permission_denied.html')


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request):
        profile = self.get_queryset().first()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
