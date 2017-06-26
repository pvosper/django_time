from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from timeapp.models import Event
from timeapp.forms import EventForm


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
    values = request.META.items()
    values.sort()
    return render(request, 'meta_detail.html', {'values': values})
