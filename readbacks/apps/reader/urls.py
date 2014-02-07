from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView
from readbacks.apps.reader.models import Grade, Unit, Reading, Paragraph
from readbacks.apps.reader.views import UnitsView, ReadingsView, ParagraphsView

urlpatterns = patterns('',
    #Shouldn't the urlconf below bring up the front page (as opposed to the 'grades' page?)
    
    url(
        r'^grades/$',
        ListView.as_view(
            model=Grade,
            context_object_name='grades',
            template_name='reader/grades.html'
        ),
        name='grades'
    ),
    

    #url(r'^grades/$', GradesView.as_view(), name='grades'),

    url(r'^units/(?P<pk>\d+)$', UnitsView.as_view(), name='units'),

    url(r'^readings/(?P<pk>\d+)$', ReadingsView.as_view(), name='readings'),
    
    url(r'^paragraph/(?P<pk>\d+)$', ParagraphsView.as_view(), name='paragraphs'),

    url(
        r'^sample/(?P<pk>\d+)$',
        TemplateView.as_view(template_name='reader/sample.html'),
        name='sample'
    ),   
)
