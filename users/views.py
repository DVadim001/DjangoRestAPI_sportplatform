from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render, redirect

from .forms import UserProfileForm, UserSettingsForm
from .models import UserProfile

from django.db.models import Q


# Просмотр профиля пользователя
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Убедитесь, что 'profile' ведет к нужному URL
    else:
        form = UserProfileForm(instance=profile)

    # Если 'user_profile' не используется в шаблоне, эту строку можно опустить
    user_profile = UserProfile.objects.get(user=request.user)

    # Передача формы и объекта профиля в контекст шаблона
    context = {
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'users/profile.html', context)


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('users:login')
    else:
        form = UserProfileForm
    context = {'form': form}
    return render(request, 'users/register.html', context)


# Логин пользователя
def login(request):
    pass


# Вывод всех пользователей
def get_all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin/users_list.html', context)


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
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=profile)

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

# Сброс пароля

# Для суперпользователя: просмотр списка пользователей, управление статусами

# Для суперпользователя: аналитика пользовательского поведения (сбор и анализ данных о взаимодействии пользователей с сайтом)
