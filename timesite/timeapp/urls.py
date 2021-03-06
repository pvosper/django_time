from django.conf.urls import url
from timeapp.views import site_index,\
    event_index,\
    event_detail,\
    event_edit,\
    event_new,\
    meta_detail,\
    set_timezone


urlpatterns = [
    url(r'^$',
        site_index,
        name="site_index"),
    url(r'^event/index/$',  # 'event/index/'
        event_index,
        name='event_index'),
    url(r'^event/(?P<event_id>\d+)/$',  # 'event/16/'
        event_detail,
        name='event_detail'),
    url(r'^event/(?P<pk>\d+)/edit/$',  # 'event/16/edit/'
        event_edit,
        name='event_edit'),
    url(r'^event/new/$',  # 'event/new/'
        event_new,
        name='event_new'),
    url(r'^meta/$',  # 'meta/'
        meta_detail,
        name='meta_detail'),
    url(r'^timezone/$',  # 'timezone/'
        set_timezone,
        name='set_timezone'),

]
