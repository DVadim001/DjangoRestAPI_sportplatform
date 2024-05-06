from django.shortcuts import render
from .models import Result, Event
from rest_framework import viewsets
from .serializers import EventSerializer, ResultSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


def result_list(request):
    results = Result.objects.all()
    context = {'results': results}
    return render(request, 'results/result_list.html', context)


def event_results(request, event_id):
    results = Result.objects.filter(event__id=event_id).order_by('position')
    event = Event.objects.get(id=event_id)
    context = {'results': results, 'event': event}
    return render(request, 'results/event_results.html', context)
