from django.contrib import admin
from .models import Event, Stand


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'name']
    search_fields = ['name']
