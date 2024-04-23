from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls',  namespace='users')),
    path('', views.main_view, name='main'),  # URL для главной страницы
    path('search/', views.global_search, name='global_search')

]
