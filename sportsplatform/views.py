from django.shortcuts import render
from users.models import UserProfile
from events.models import Event, Participant
from django.db.models import Q


def main_view(request):
    # Получить данные из приложения users
    random_users = UserProfile.objects.order_by('?')[:10]

    # Получить данные из других приложений аналогичным образом

    context = {
        'users_data': random_users,
        # Добавить другие данные в контекст
    }
    return render(request, 'main.html', context)


# Поиск общий
def global_search(request):
    query = request.GET.get('q', '')

    # Поиск среди пользователей по именам, адресу электронной почты и т.д.
    user_profiles_results = UserProfile.objects.filter(
        Q(user__username__icontains=query) |
        Q(user__email__icontains=query)
    )

    # Поиск среди событий по имени, описанию и локации
    events_result = Event.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(location__icontains=query)
    )

    # Поиск событий по тэгам
    tagged_events_result = Event.objects.filter(
        Q(tags__name__icontains=query)
    ).distinct()

    # Поиск участников события по имени пользователя
    participants_results = Participant.objects.filter(
        Q(user__username__icontains=query)
    )

    context = {
        'user_profiles_results': user_profiles_results,
        'events_result': events_result,
        'tagged_events_result': tagged_events_result,
        'participants_results': participants_results
    }
    return render(request, 'search_result.html', context)
