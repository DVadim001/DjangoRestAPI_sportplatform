from .models import UserActivityLog

def log_user_action(request, action, metadata=None):
    ip = get_client_ip(request)
    log = UserActivityLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action=action,
        ip_address=ip,
        metadata=metadata or {}
    )
    return log

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
