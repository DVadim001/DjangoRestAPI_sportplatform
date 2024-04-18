from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Event
from .forms import EventForm


# Создание нового события
def create_new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')
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
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:event_details', event_id=event.id)
    else:
        form = EventForm(instance=event)
    context = {'form': form, 'event': event}
    return render(request, 'events/edit_event.html', context)


# Удаление определённого события (только создатель, главные админы и (возможно!) доверенные лица )
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    context = {'event': event}
    return render(request, 'events/confirm_delete.html', context)
