from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Registration
from .forms import RegistrationForm
from rest_framework import viewsets
from .serializers import RegistrationSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

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


# registrations/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'registrations'

router = DefaultRouter()
router.register(r'api/registrations', views.RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('create/', views.register_for_event, name='register_for_event'),
    path('', include(router.urls)),
    path('cancel/<int:registration_id>/', views.cancel_registration, name='cancel_registration'),


]
