from .models import Message

def user_messages(request):
    if request.user.is_authenticated:
        return {
            'user_messages': Message.objects.filter(recipient=request.user).order_by('-sent_at')[:5]
        }
    return {}
