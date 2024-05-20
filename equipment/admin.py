from django.contrib import admin
from .models import Equipment, EquipmentReservation


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('status',)


@admin.register(EquipmentReservation)
class EquipmentReservationAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'user', 'event', 'start_date', 'end_date', 'created_at')
    search_fields = ('equipment__name', 'user__username', 'event__name')
    list_filter = ('start_date', 'end_date')
