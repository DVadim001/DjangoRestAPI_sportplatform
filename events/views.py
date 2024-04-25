from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from  django.contrib import messages

from .models import Event, Participant
from .forms import EventForm


# Создание нового события
@login_required
def create_new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user # Установка создателя события
            event.save()
            return redirect('events:events_list')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'events/create_event.html', context)


# Вывод списка всех событий
def events_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/events_list', context)


# Вывод списка категорий событий
def category_list(request):
    categories = Event.objects.values('category').distinct()
    context = {'categories': categories}
    return render(request, 'events/category_list.html', context)


# Поиск события по заданным параметрам
def search_event(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        events = Event.objects.none()
    context = {'events': events}
    return render(request, 'events/search_results.html', context)


# Просмотр деталий конкретного события
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {'event': event}
    return render(request, 'events/event_details.html', context)


# Редактирование определённого события (только создатель, главные админы и (возможно!) доверенные лица )
@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user != event.organizer and not request.user.is_superuser:
        return HttpResponseForbidden("Недостаточно прав для редактирования данного события.")

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:event_details', event_id=event.id)
    else:
        form = EventForm(instance=event)
    context = {'form': form, 'event': event}
    return render(request, 'events/edit_event.html', context)


@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        # Проверка, зарегистрирован ли пользователь
        if Participant.objects.filter(event=event, user=request.user).exists():
            messages.error(request, "Вы уже зарегистрированы на это событие.")
        else:
            # Создание записи участника
            Participant.objects.create(user=request.user, event=event, status='registered')
        return redirect('events:event_details', event_id=event.id)
    else:
        context = {'event': event}
        return render(request, 'events/register_for_event.html', context)


# Удаление определённого события (только создатель, главные админы и (возможно!) доверенные лица )
@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user != event.organizer and not request.user.is_superuser:
        return HttpResponseForbidden("Недостаточно прав для удаления данного события.")

    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    context = {'event': event}
    return render(request, 'events/confirm_delete.html', context)
