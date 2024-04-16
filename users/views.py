from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login as auth_login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import CustomUserCreationForm, UserProfileUpdateForm, UserSettingsForm
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSettingsSerializer

from rest_framework import viewsets


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSettingsSerializer


# Просмотр профиля пользователя
@login_required
def profile_view(request, user_id):
    # Получаем профиль пользователя или возвращаем 404, если он не найден
    user_profile = get_object_or_404(UserProfile, user__id=user_id)

    # Проверяем, имеет ли текущий пользователь права на просмотр этой страницы
    if request.user.id != user_profile.user.id and not request.user.is_superuser:
        return redirect('permission_danied')

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile_view', user_id=user_id)
    else:
        form = UserProfileUpdateForm(instance=user_profile)

    context = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'users/profile.html', context)


# Логин пользователя
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('users:profile')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('users:profile')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


# Вывод всех пользователей
def get_all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users_list.html', context)


# Поиск пользователя по фильтру (по имени и т.д.)
def search_user_by_filter(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query)) | Q(email__icontains=query)
    else:
        users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/search_results.html', context)


# Смена пароля
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user:profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'users/change_password.html', context)


# Редактирование профиля
@login_required
def edit_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileUpdateForm(instance=profile)

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)


# Изменение настроек профиля
@login_required
def update_profile_settings(request):
    profile = request.user.userprofile
    if request.method == "POST":
        form = UserSettingsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserSettingsForm(instance=profile)
    context = {'form': form}
    return render(request, 'users/settings.html', context)


# Выход пользователя
def logout_request(request):
    logout(request)
    return redirect('/')

# Сброс пароля

# Для суперпользователя: просмотр списка пользователей, управление статусами

# Для суперпользователя: аналитика пользовательского поведения
# (сбор и анализ данных о взаимодействии пользователей с сайтом)
