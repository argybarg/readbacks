from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView
from readbacks.apps.reader.models import Grade, Unit, Reading, Paragraph
from readbacks.apps.reader.views import UnitsView, ReadingsView, ParagraphsView

#  Do we change templateview to listview as seen in 2nd video?
#  (see url listview.as_view commented out below)     
#  NEXT ADD IN CODE in grades.html file for PAGINATION?


"""
/

/reader/grade/<grade_level>/unit/<unit_slug>/reading/<reading_slug>/paragraph/<code>

/reader

xxxxx/reader/grade/<grade_level>/ =>  units list


/reader/grade/<grade_level>/unit/<unit_slug>/  readings list

/reader/grade/<grade_level>/unit/<unit_slug>/reading/<reading_slug>/  paragraph list

"""

urlpatterns = patterns(
    '',

    url(
        r'^$',
        ListView.as_view(
            model=Grade,
            context_object_name='grades',
            template_name='reader/grades.html'
        ),
        name='grades'
    ),

    url(
        r'^grade/(?P<grade_level>\d+)$',
        UnitsView.as_view(),
        name='units'
    ),

    url(
        r'^grade/(?P<grade_level>\d+)/unit/(?P<unit_slug>[-\w]+)$',
        ReadingsView.as_view(),
        name='readings'
    ),

    url(
        r'^grade/(?P<grade_level>\d+)/unit/(?P<unit_slug>[-\w]+)/reading/(?P<reading_slug>[-\w]+)$',
        ParagraphsView.as_view(),
        name='paragraphs'
    ),

    url(
        r'^sample/(?P<pk>\d+)$',
        TemplateView.as_view(template_name='reader/sample.html'),
        name='sample'
    ),   
)
