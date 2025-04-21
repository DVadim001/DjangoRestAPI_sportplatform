from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login as auth_login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserCreationForm, UserProfileUpdateForm, UserSettingsForm
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSettingsSerializer
from communication.models import Message, Notification
from clubs.models import Membership

from rest_framework import viewsets
from phonenumber_field.phonenumber import to_python


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSettingsSerializer


# Страна по коду телефону
def view_country_by_phone(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Получаем профиль пользователя
    phone_number = to_python(user_profile.phone_number)  # Преобразуем номер телефона
    country = None
    if phone_number and phone_number.is_valid():
        country = phone_number.region_code_for_number()  # Получаем код страны

    context = {
        'country': country,
        'phone_number': phone_number
    }
    return render(request, 'users:edit_profile', context)


# Просмотр профиля пользователя
@login_required
def profile_view(request, user_id):
    # Используем get_object_or_404 для получения объекта User
    user = get_object_or_404(User, pk=user_id)

    # Попытаемся получить или создать UserProfile
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    # Проверяем, имеет ли текущий пользователь права на просмотр этой страницы
    if request.user.id != user.id and not request.user.is_superuser:
        return render(request, 'users/permission_denied.html')

    # Получаем сообщения и уведомления для пользователя
    messages_received = Message.objects.filter(recipient=user)
    notifications = Notification.objects.filter(user=user)

    # Получаем клубы, учитывая связанные объекты для оптимизации запросов
    clubs = Membership.objects.filter(user=user).select_related('club')

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile_view', user_id=user_id)
    else:
        form = UserProfileUpdateForm(instance=user_profile)

    context = {
        'form': form,
        'user_profile': user_profile,
        'messages_received': messages_received,
        'notifications': notifications,
        'clubs': clubs
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
    return render(request, 'registration/login.html', context)


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile. objects.create(user=user)
            auth_login(request, user)
            return redirect('users:profile')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


# Вывод всех пользователей
@login_required
def get_all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users_list.html', context)


# Смена пароля
@login_required
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
    # Получаем или создаём профиль пользователя, усли он не существует
    profile, create = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile_view', user_id=request.user.id)
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
