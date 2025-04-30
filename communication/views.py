from django.shortcuts import render, get_object_or_404, redirect
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

from .models import Message, Notification
from .serializers import MessageSerializer, NotificationSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

@login_required
def message_list(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'communication/message_list.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'communication/message_detail.html', {'message': message})

@login_required
def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('communication:message_list')
    else:
        form = MessageForm()
    return render(request, 'communication/message_form.html', {'form': form})

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notification_list.html', {'notifications': notifications})

@login_required
def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'notification_detail.html', {'notification': notification})

@login_required
def notification_confirm_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        notification.delete()
        return redirect('communication:notification_list')
    return render(request, 'notification_confirm_delete.html', {'notification': notification})


@login_required
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('communication:message_list')
    return render(request, 'communication/message_confirm_delete.html', {'message': message})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
