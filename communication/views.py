from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .forms import MessageForm
from .models import Message, Notification
from .serializers import MessageSerializer, NotificationSerializer


class MessgeViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.filter(is_seen=False)
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Просмотр списка сообщений
def message_list(request):
    messages = Message.objects.filter(user=request.user)
    context = {'messages': messages}
    return render(request, 'communication/message_list.html', context)


# Детали сообщения
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, user=request.user)
    context = {'message': message}
    return render(request, 'communication/message_detail.html', context)


@login_required
# Создание сообщения
def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('communication:message_detail', pk=message.pk)
    else:
        form = MessageForm()
    context = {'form': form, 'form_title': 'Написать сообщение'}
    return render(request, 'communication/message_form.html', context)


# Редактирование сообщений
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('communication:message_detail', pk=message.pk)
    else:
        form = MessageForm(instance=message)
    context = {'form': form}
    return render(request, 'communication/message_form.html', context)


@require_POST
# Удаление сообщения
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk, user=request.user)
    message.delete()
    return redirect('communication:message_list')


# Просмотр списка уведомлений
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user)
    context = {'notifications': notifications}
    return render(request, 'communication/notification_list.html', context)


# Отметить уведомление как прочитанное
@require_POST
def mark_notification_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('communication:notification_list')


# Удаление уведомления
@login_required
def notification_delete(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    if request.method == 'POST':
        notification.delete()
        return redirect('communication:notification_list')
    context = {'notification': notification}
    return render(request, 'communication/notification_confirm_delete.html', context)
