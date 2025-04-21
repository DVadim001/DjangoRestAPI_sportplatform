from rest_framework import viewsets
from django.shortcuts import render
from django.db.models import Count
from .models import PageVisit, UserAction
from .serializers import PageVisitSerializer, UserActionSerializer


class PageVisitViewSet(viewsets.ModelViewSet):
    queryset = PageVisit.objects.all()
    serializer_class = PageVisitSerializer


class UserActionViewSet(viewsets.ModelViewSet):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer


def page_visits_chart(request):
    visits = PageVisit.objects.extra(select={'day': 'date(timestamp)'}).values('day').annotate(
        count=Count('id')).order_by('day')
    labels = [visit['day'].strftime('%Y-%m-%d') for visit in visits]
    data = [visit['count'] for visit in visits]

    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'analytics/page_visits.html', context)


def user_actions_chart(request):
    actions = UserAction.objects.extra(select={'day': 'date(timestamp)'}).values('day', 'action_type').annotate(
        count=Count('id')).order_by('day')
    labels = sorted(set([action['day'].strftime('%Y-%m-%d') for action in actions]))
    action_types = sorted(set([action['action_type'] for action in actions]))

    data = {action_type: [0] * len(labels) for action_type in action_types}

    for action in actions:
        day_index = labels.index(action['day'].strftime('%Y-%m-%d'))
        data[action['action_type']][day_index] = action['count']

    context = {
        'labels': labels,
        'data': data,
        'action_types': action_types,
    }
    return render(request, 'analytics/user_actions.html', context)
