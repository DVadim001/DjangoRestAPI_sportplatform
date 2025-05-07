from rest_framework import viewsets
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate


from .models import PageVisit, UserAction
from .serializers import PageVisitSerializer, UserActionSerializer


class PageVisitViewSet(viewsets.ModelViewSet):
    queryset = PageVisit.objects.all()
    serializer_class = PageVisitSerializer



class UserActionViewSet(viewsets.ModelViewSet):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer



def page_visits_chart(request):
    data = (
        PageVisit.objects
        .annotate(date=TruncDate('timestamp'))
        .values('date')
        .annotate(visits=Count('id'))
        .order_by('date')
    )

    labels = [item['date'].isoformat() for item in data]
    values = [item['visits'] for item in data]

    return render(request, 'analytics/page_visits.html', {
        'labels': labels,
        'data': values
    })


def user_actions_chart(request):
    data = (
        UserAction.objects
        .annotate(date=TruncDate('timestamp'))
        .values('action_type', 'date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    dates = sorted({item['date'].isoformat() for item in data})
    action_types = sorted({item['action_type'] for item in data})

    datasets = []
    for idx, action in enumerate(action_types):
        action_data = []
        for date in dates:
            count = next(
                (item['count'] for item in data if item['action_type'] == action and item['date'].isoformat() == date),
                0
            )
            action_data.append(count)

        datasets.append({
            'label': action,
            'data': action_data,
            'borderColor': f'rgba({(idx * 60) % 255}, 99, 132, 1)',
            'borderWidth': 1
        })

    return render(request, 'analytics/user_actions.html', {
        'labels': dates,
        'datasets': datasets,
    })
