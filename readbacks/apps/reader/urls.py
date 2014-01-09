from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name='reader/grades.html'),
        name='grades'
    ),
    url(
        r'^passages/$',
        TemplateView.as_view(template_name='reader/passages.html'),
        name='passages'
    ),
    url(
        r'^units/$',
        TemplateView.as_view(template_name='reader/units.html'),
        name='units'
    )
)
