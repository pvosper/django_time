from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from timeapp.models import Event
from timeapp.forms import EventForm
import logging

# create logger with module name
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
log_file_name = __name__ + '.log'
fh = logging.FileHandler(log_file_name)
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

def site_index(request):
    """Home page - Calendar"""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'site_index.html', context)


def event_index(request):
    """Display all events"""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event_index.html', context)


def event_detail(request, event_id):
    """Display a single event
    by getting all posts then filtering by pk"""
    events = Event.objects.all()
    try:
        event = events.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404
    context = {'event': event}
    return render(request, 'event_detail.html', context)


def event_edit(request, pk):
    """Edit Event"""
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = {'event': event}
            return render(request, 'event_detail.html', context)
        else:
            pass
    else:
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form})

def event_new(request):
    """Edit Event"""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            # save form
            event = form.save(commit=False)
            event.save()
            # then create site_index
            events = Event.objects.all()
            context = {'events': events}
            return render(request, 'site_index.html', context)
    else:
        form = EventForm()
    return render(request, 'event_edit.html', {'form': form})

def meta_detail(request):
    """Display META values"""
    # path get_host get_full_path is_secure
    values = request.META.items()
    # create list of formatted strings
    meta_items = []
    meta_items.append("{}: {}".format('request.path', request.path))
    meta_items.append("{}: {}".format('request.get_host()', request.get_host()))
    meta_items.append("{}: {}".format('request.get_full_path()', request.get_full_path()))
    meta_items.append("{}: {}".format('request.is_secure()', request.is_secure()))
    for value in values:
        meta_items.append("{}: {}".format(value[0], value[1]))
    return render(request, 'meta_detail.html', {'meta_items': meta_items})

from django.shortcuts import redirect, render

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'set_timezone.html', {'timezones': pytz.common_timezones})
