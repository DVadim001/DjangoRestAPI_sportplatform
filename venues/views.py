from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Venue
from .forms import VenueForm
from rest_framework import viewsets
from .serializers import VenueSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

@login_required
def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'venues/venue_list.html', {'venues': venues})

@login_required
def venue_detail(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    return render(request, 'venues/venue_detail.html', {'venue': venue})

@login_required
def venue_create(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.creator = request.user
            venue.save()
            return redirect('venues:venue_detail', pk=venue.pk)
    else:
        form = VenueForm()
    return render(request, 'venues/venue_form.html', {'form': form})

@login_required
def venue_edit(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venues:venue_detail', pk=venue.pk)
    else:
        form = VenueForm(instance=venue)
    return render(request, 'venues/venue_form.html', {'form': form})

@login_required
def venue_delete(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        venue.delete()
        return redirect('venues:venue_list')
    return render(request, 'venues/venue_confirm_delete.html', {'venue': venue})