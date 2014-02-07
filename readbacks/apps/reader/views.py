
from django.views.generic import TemplateView, ListView, DetailView
from readbacks.apps.reader.models import Grade, Unit, Reading, Paragraph

#class GradesView(ListView):
#	model = Grade
#	context_object_name = 'grades'
#	template_name = 'reader/grades.html'

class UnitsView(ListView):
	model = Unit
	context_object_name = 'units'
	template_name = 'reader/units.html'

class ReadingsView(ListView):
	model = Reading
	context_object_name = 'readings'
	template_name = 'reader/readings.html'

class ParagraphsView(ListView):
	model = Paragraph
	context_object_name = 'paragraphs'
	template_name = 'reader/paragraphs.html'
