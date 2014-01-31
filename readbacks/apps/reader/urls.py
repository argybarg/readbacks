from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView
#, DetailView
from readbacks.apps.reader.models import Grade

#  Do we change templateview to listview as seen in 2nd video?
#  (see url listview.as_view commented out below)     
#  NEXT ADD IN CODE in grades.html file for PAGINATION?
urlpatterns = patterns('',
#   url(r'^$', 
#    detailview.as_view(context_object_name="Grades"
#    model = Grades,    
#    template_name='reader/grades.html'),
   
    url(
        r'^$',
        ListView.as_view(
            model = Grade,
            context_object_name = 'grades',
            template_name='reader/grades.html'
        ),
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
    ),
    url(
        r'^sample/$',
        TemplateView.as_view(template_name='reader/sample.html'),
        name='sample'
    ),   
)
