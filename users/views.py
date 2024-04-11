from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile


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
