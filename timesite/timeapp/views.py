from django.shortcuts import render
from timeapp.models import Event


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