from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('simon.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home', name='home'),
    url(r'^simon/$', 'simon', name='simon'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
