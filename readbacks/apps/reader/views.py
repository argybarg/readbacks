
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

    def get_queryset(self):
        readings = Reading.objects.filter(unit__grade__level=self.kwargs['grade_level'], unit__slug=self.kwargs['unit_slug'])
        return readings

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['unit'] = Unit.objects.get(grade__level=self.kwargs['grade_level'], slug=self.kwargs['unit_slug'])
        context['grade_level'] = self.kwargs['grade_level']
        return context


class ParagraphsView(ListView):
    model = Paragraph
    context_object_name = 'paragraphs'
    template_name = 'reader/paragraphs.html'

    def get_queryset(self):
        paragraphs = Paragraph.objects.filter(reading__unit__grade__level=self.kwargs['grade_level'], reading__unit__slug=self.kwargs['unit_slug'], 
        		reading__slug=self.kwargs['reading_slug'])
        return paragraphs

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['reading'] = Reading.objects.get(unit__grade__level=self.kwargs['grade_level'], unit__slug=self.kwargs['unit_slug'],
        		slug=self.kwargs['reading_slug'])
        context['grade_level'] = self.kwargs['grade_level']
        context['unit_slug'] = self.kwargs['unit_slug']

        return context


class ParagraphDetailView(DetailView):
    model = Paragraph
    context_object_name = 'paragraph'
    template_name = 'reader/paragraph_detail.html'




"""
class Nav_PagesView(ListView):
    model = Unit
    context_object_name = 'nav_pages'
    template_name = 'reader/nav_page.html'

    def get_queryset(self):
        grades = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
        units = Unit.objects.filter(grade__level=self.kwargs['grade_level'])
        nav_pages = [grades, units]
        return nav_pages

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['grade_level'] = self.kwargs['grade_level']
        return context
"""

