from analytics.models import PageVisit

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем только GET-запросы (можно изменить на любые, если нужно)
        if request.method == "GET":
            PageVisit.objects.create(
                path=request.path,
                method=request.method,
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                user=request.user if request.user.is_authenticated else None
            )

        response = self.get_response(request)
        return response
