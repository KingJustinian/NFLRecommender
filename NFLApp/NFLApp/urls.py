from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NFLApp.views.home', name='home'),
    # url(r'^NFLApp/', include('NFLApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^main/', include('main.urls')),      
    url(r'^admin/', include(admin.site.urls)),
)
