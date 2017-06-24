from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    event_time = models.DateTimeField(auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title