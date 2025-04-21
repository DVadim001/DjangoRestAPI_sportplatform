from django.contrib import admin
from .models import Event, Participant, EventImage


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'location', 'organizer')
    list_filter = ('start_time', 'end_time', 'location')
    search_fields = ('name', 'description')


admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(EventImage)
