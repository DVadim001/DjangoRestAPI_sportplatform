from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Schedule, Category
from .forms import ScheduleForm
from .serializers import ScheduleSerializer, CategorySerializer

from rest_framework import viewsets


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Вывод всех планирований
@login_required
def schedule_list(request):
    schedules = Schedule.objects.filter(user=request.user)
    context = {'schedules': schedules}
    return render(request, 'schedules/schedule_list.html', context)


# Вывод деталей одного планирования
@login_required
def schedule_detail(request, schedule_id):
    schedule = get_object_or_404(id=schedule_id, user=request.user)
    context = {'schedule': schedule}
    return render(request, 'schedules/schedule_detail.html', context)


# Создание планирования
@login_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('schedules:schedule_list')
    else:
        form = ScheduleForm()
    context = {'form': form}
    return render(request, 'schedules/schedule_form.html', context)


# Изменение планирования
@login_required
def schedule_update(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id, user=request.user)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedules:schedule_detail', schedule_id=schedule.id)
    else:
        form = ScheduleForm(instance=schedule)
    context = {'form': form}
    return render(request, 'schedules/schedule_form.html', context)


# Удаление планирования
@login_required
def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id, user=request.user)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedules:schedule_list')
    context = {'schedule': schedule}
    return render(request, 'schedules/schedule_confirm_delete.html', context)
