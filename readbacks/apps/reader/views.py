
from django.views.generic import TemplateView, ListView, DetailView
from readbacks.apps.reader.models import Grade, Unit, Reading, Paragraph

#class GradesView(ListView):
#   model = Grade
#   context_object_name = 'grades'
#   template_name = 'reader/grades.html'


class UnitsView(ListView):
    model = Unit
    context_object_name = 'units'
    template_name = 'reader/units.html'

    def get_queryset(self):
        units = Unit.objects.filter(grade__level=self.kwargs['grade_level'])
        return units

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['grade_level'] = self.kwargs['grade_level']
        return context


class ReadingsView(ListView):
    model = Reading
    context_object_name = 'readings'
    template_name = 'reader/readings.html'


class ParagraphsView(ListView):
    model = Paragraph
    context_object_name = 'paragraphs'
    template_name = 'reader/paragraphs.html'
