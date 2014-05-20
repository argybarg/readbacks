from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
from readbacks.apps.reader.models import Grade, Unit, Reading, Paragraph
from readbacks.apps.reader.views import UnitsView, ReadingsView, ParagraphsView, ParagraphDetailView
from readbacks.apps.reader.views import UnitCreate, UnitUpdate, UnitDelete
from readbacks.apps.reader.views import ReadingCreate, ReadingUpdate, ReadingDelete


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
        r'^paragraph/(?P<pk>\d+)$', 
        ParagraphDetailView.as_view(),
        name='paragraph_detail'
    ),

    url(
        r'unit/add/$', UnitCreate.as_view(), name='unit_add'
    ),

    url(
        r'unit/(?P<pk>\d+)/$', UnitUpdate.as_view(), name='unit_update'
    ),

    url(
        r'unit/(?P<pk>\d+)/delete/$', UnitDelete.as_view(), name='unit_delete'
    ),  

    url(
        r'reading/add/$', ReadingCreate.as_view(), name='reading_add'
    ),

    url(
        r'reading/(?P<pk>\d+)/$', UnitUpdate.as_view(), name='reading_update'
    ),

    url(
        r'reading/(?P<pk>\d+)/delete/$', UnitDelete.as_view(), name='reading_delete'
    ), 
)
