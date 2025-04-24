from django.shortcuts import render, get_object_or_404, redirect
from .models import Message, Notification
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def message_list(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'message_list.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'message_detail.html', {'message': message})

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
    return render(request, 'message_form.html', {'form': form})

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
