from django.contrib import admin
from .models import Club, Membership


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'club', 'date_joined', 'is_admin']
    list_filter = ['club', 'is_admin']
    search_fields = ['user__username', 'club__name']
