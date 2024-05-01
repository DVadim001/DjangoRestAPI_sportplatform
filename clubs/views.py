from django.shortcuts import render, redirect, get_object_or_404
from .models import Club
from .forms import ClubForm


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
            return redirect('clubs:club_detail', pk=club.pk)
    else:
        form = ClubForm()
    context = {'form': form}
    return render(request, 'clubs/club_form', context)


# Редактирование клуба
def club_edit(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            club = form.save()
            return redirect('club:club_detail', pk=club.pk)
    else:
        form = ClubForm(instance=club)
    context = {'form': form}
    return render(request, 'clubs/club_form.html', context)
