from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Result, Event
from .forms import ResultForm

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ResultSerializer

@login_required
def result_list(request):
    results = Result.objects.all()
    return render(request, 'results/result_list.html', {'results': results})

@login_required
def event_results(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    results = Result.objects.filter(event=event).order_by('position')
    return render(request, 'results/event_results.html', {'event': event, 'results': results})

@login_required
def add_result(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.event = event
            result.participant = request.user
            result.save()
            return redirect('results:event_results', event_id=event.id)
    else:
        form = ResultForm()
    return render(request, 'results/add_result.html', {'form': form, 'event': event})

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(participant=self.request.user)
