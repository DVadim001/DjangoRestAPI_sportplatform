from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Membership
from .forms import ClubForm
from .serializers import ClubSerializer, MembershipSerializer

from rest_framework import viewsets


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


# Просмотр списка клубов
def club_list(request):
    clubs = Club.objects.all()
    context = {'clubs': clubs}
    return render(request, 'clubs/club_list.html', context)


# Просмотр деталей клуба
def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    context = {'club': club}
    return render(request, 'clubs/club_detail.html', context)


# Создание клуба
def club_create(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save()
            Membership.objects.create(user=request.user, club=club, is_admin=True)
            return redirect('users:profile_view', user_id=request.user.id)
    else:
        form = ClubForm()
    context = {'form': form}
    return render(request, 'clubs/club_form.html', context)


# Редактирование клуба
def club_edit(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            club = form.save()
            return redirect('clubs:club_detail', pk=club.pk)
    else:
        form = ClubForm(instance=club)
    context = {'form': form}
    return render(request, 'clubs/club_form.html', context)


# Удаление клуба
def club_delete(request, pk):
    club = get_object_or_404(Club, id=pk)
    if request.method == 'POST':
        club.delete()
        return redirect('clubs:club_list')
    context = {'club': club}
    return render(request, 'clubs/club_confirm_delete.html', context)
