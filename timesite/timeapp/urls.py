from django.conf.urls import url
from timeapp.views import site_index, event_index, event_detail, event_edit


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

]
