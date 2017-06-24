from django import forms
from timeapp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time',)
