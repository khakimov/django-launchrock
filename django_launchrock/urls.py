from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'launch.views.signup', name='signup'),
    url(r'^done/$', 'launch.views.done', name='done'),
)