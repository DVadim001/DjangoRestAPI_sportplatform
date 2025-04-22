from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Registration
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import RegistrationSerializer

from django.views.decorators.http import require_POST
from django.contrib import messages


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


@login_required
def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id, user=request.user)

    if request.method == 'POST':
        registration.delete()
        return redirect('registrations:registration_list')

    return render(request, 'registrations/registration_confirm_cancel.html', {
        'registration': registration
    })


@login_required
def registration_list(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'registrations/registration_list.html', {'registrations': registrations})


@login_required
def register_for_event(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()
            return redirect('registrations:registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registrations/registration_form.html', {'form': form})
