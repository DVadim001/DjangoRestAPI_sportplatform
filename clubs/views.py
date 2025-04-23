from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Club, Membership
from .forms import ClubForm
from .serializers import ClubSerializer, MembershipSerializer
from rest_framework import viewsets
from analytics.models import UserAction  # если используешь аналитику


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


@login_required
def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})


@login_required
def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request, 'clubs/club_detail.html', {'club': club})


@login_required
def club_create(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save()
            Membership.objects.create(user=request.user, club=club, is_admin=True)

            # логирование действия
            UserAction.objects.create(
                user=request.user,
                action_type='content_interaction',
                additional_info=f'Создан клуб: {club.name}'
            )

            messages.success(request, 'Клуб успешно создан!')
            return redirect('clubs:club_detail', pk=club.pk)
    else:
        form = ClubForm()
    return render(request, 'clubs/club_form.html', {'form': form})


@login_required
def club_edit(request, pk):
    club = get_object_or_404(Club, pk=pk)

    # Проверка, что пользователь — админ этого клуба
    if not Membership.objects.filter(user=request.user, club=club, is_admin=True).exists():
        messages.error(request, 'У вас нет прав для редактирования этого клуба.')
        return redirect('clubs:club_detail', pk=pk)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            messages.success(request, 'Клуб успешно обновлён!')
            return redirect('clubs:club_detail', pk=club.pk)
    else:
        form = ClubForm(instance=club)
    return render(request, 'clubs/club_form.html', {'form': form})


@login_required
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)

    # Проверка, что пользователь — админ этого клуба
    if not Membership.objects.filter(user=request.user, club=club, is_admin=True).exists():
        messages.error(request, 'У вас нет прав для удаления этого клуба.')
        return redirect('clubs:club_detail', pk=pk)

    if request.method == 'POST':
        club.delete()
        messages.success(request, 'Клуб удалён.')
        return redirect('clubs:club_list')
    return render(request, 'clubs/club_confirm_delete.html', {'club': club})
