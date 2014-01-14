from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name='reader/grades.html'),
        name='grades'
    ),
    url(
        r'^readings/$',
        TemplateView.as_view(template_name='reader/readings.html'),
        name='readings'
    ),
    url(
        r'^units/$',
        TemplateView.as_view(template_name='reader/units.html'),
        name='units'
    ),
    url(
        r'^paragraph/$',
        TemplateView.as_view(template_name='reader/paragraph.html'),
        name='paragraph'
    )
    
)
