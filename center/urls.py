from django.conf.urls import patterns, url


urlpatterns = patterns('center.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)
