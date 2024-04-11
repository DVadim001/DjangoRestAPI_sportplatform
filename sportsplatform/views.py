from django.shortcuts import render
from users.models import UserProfile


def main_view(request):
    # Получить данные из приложения users
    random_users = UserProfile.objects.order_by('?')[:10]

    # Получить данные из других приложений аналогичным образом

    context = {
        'users_data': random_users,
        # Добавить другие данные в контекст
    }
    return render(request, 'main.html', context)
