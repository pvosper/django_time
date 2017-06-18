from django.contrib import admin
from timeapp.models import Event

class EventAdmin(admin.ModelAdmin):
    fields : ('title',
              'description',
              'event_start',
              'even_end', )

admin.site.register(Event, EventAdmin)
