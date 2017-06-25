from django import forms
from timeapp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'event_time',)

'''Notes:

https://stackoverflow.com/questions/2913700/django-forms-timefield-validation

calendar_widget = forms.widgets.DateInput(attrs={'class': 'date-pick'}, format='%m/%d/%Y')
time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=calendar_widget)
    start_time = forms.TimeField(required=False, widget=time_widget, help_text='ex: 10:30AM', input_formats=valid_time_formats)
    ...
    
See the first note under the table of directives here:

http://docs.python.org/library/time.html#time.strftime.'''

