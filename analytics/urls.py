from django.urls import path
from .views import page_visits_chart, user_actions_chart
from django.shortcuts import render

app_name = 'analytics'

urlpatterns = [
    path('charts/page_visits/', page_visits_chart, name='page_visits_chart'),
    path('charts/user_actions/', user_actions_chart, name='user_actions_chart'),
    path('', lambda request: render(request, 'analytics/analytics_home.html'), name='analytics_home'),
]
