# Django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Django REST Framework
from rest_framework import viewsets, permissions

# Внутренние модули
from .models import Equipment, EquipmentReservation
from .forms import EquipmentForm, EquipmentReservationForm
from .serializers import EquipmentSerializer, EquipmentReservationSerializer

from analytics.utils import log_user_action

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EquipmentReservationViewSet(viewsets.ModelViewSet):
    queryset = EquipmentReservation.objects.all()
    serializer_class = EquipmentReservationSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment})


@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment})


@login_required
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.owner = request.user
            equipment.save()

            # логирование действия
            log_user_action(
                request,
                action="Создание оборудования",
                metadata={
                    "equipment_id": equipment.id,
                    "equipment_name": equipment.name
                }
            )

            return redirect('equipment:equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/equipment_form.html', {'form': form})


@login_required
def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/equipment/{pk}/')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment/equipment_form.html', {'form': form})


@login_required
def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return HttpResponseRedirect('/equipment/')
    return render(request, 'equipment/equipment_confirm_delete.html', {'equipment': equipment})


@login_required
def equipment_reserve(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)

    if request.method == 'POST':
        form = EquipmentReservationForm(request.POST, equipment=equipment)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.equipment = equipment
            reservation.user = request.user
            reservation.save()
            return HttpResponseRedirect(f'/equipment/{pk}/')
    else:
        form = EquipmentReservationForm(equipment=equipment)

    return render(request, 'equipment/equipment_reserve.html', {
        'form': form,
        'equipment': equipment
    })