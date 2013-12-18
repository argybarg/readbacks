from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('readbacks.apps.home.urls')),
    # url(r'^reader/', include('apps.reader.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
