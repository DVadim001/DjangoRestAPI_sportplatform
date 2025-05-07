from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Registration
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import RegistrationSerializer

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from events.models import Event
from .models import Registration

from analytics.utils import log_user_action

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

            # логирование действия
            log_user_action(
                request,
                action="Регистрация на событие",
                metadata={
                    "event_id": registration.event.id,
                    "event_name": registration.event.name,
                    "registration_id": registration.id
                }
            )

            return redirect('registrations:registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registrations/registration_form.html', {'form': form})


@login_required
@require_POST
def register_for_event_specific(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Проверка, не зарегистрирован ли уже пользователь
    if not Registration.objects.filter(user=request.user, event=event).exists():
        Registration.objects.create(user=request.user, event=event)

    return redirect('registrations:registration_list')