from django.shortcuts import render
from django.contrib import messages

from .forms import ClubForm
from .serializers import ClubSerializer, MembershipSerializer
from rest_framework import viewsets
from analytics.models import UserAction

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Club, Membership
from django.shortcuts import get_object_or_404, redirect


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
    club = get_object_or_404(Club, id=pk)
    memberships = club.membership_set.select_related('user')
    is_member = memberships.filter(user=request.user).exists()  # ⬅ добавили проверку
    return render(request, 'clubs/club_detail.html', {
        'club': club,
        'memberships': memberships,
        'is_member': is_member,  # ⬅ добавили в контекст
    })

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


@login_required
@require_POST
def join_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    # Проверка: не является ли пользователь уже участником
    if not Membership.objects.filter(user=request.user, club=club).exists():
        Membership.objects.create(user=request.user, club=club, is_admin=False)

    return redirect('clubs:club_detail', club_id=club.id)
