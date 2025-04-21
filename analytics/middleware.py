from .models import PageVisit

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            PageVisit.objects.create(
                user=request.user,
                path=request.path,
                method=request.method,
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
        return response