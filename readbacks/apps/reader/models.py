from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField

from readbacks.apps.common.utils import truncatesmart


class Grade(models.Model):
    level = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return 'Grade %s' % self.level

    def get_absolute_url(self):
        url = reverse('grades')
        return "%s" % url

    def image_path(self):
        return "reader/%s.jpg" % self.level

    #class Admin: pass


class Unit(models.Model):
    grade = models.ForeignKey(Grade)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        unique_together = ('name', 'grade')

    def __unicode__(self):
        return '%s %s' % (self.grade, self.name)

    def get_absolute_url(self):
        url = reverse('units', kwargs={'grade_level': grade.level })
        return "%s" % url

    def readings(self):
        return Reading.objects.filter(unit=self)


class Reading(models.Model):
    unit = models.ForeignKey(Unit)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return '%s,  %s' % (self.unit, self.name)

    def get_absolute_url(self):
        url = reverse('readings', kwargs={'grade_level': unit.grade.level, 'unit_slug': unit.slug })
        return "%s" % url

    def paragraphs(self):
        return Paragraph.objects.filter(reading=self)

    #class Admin: pass


class Paragraph(models.Model):
    reading = models.ForeignKey(Reading)
    text = models.CharField(max_length=1000)                            # TODO make a textfield           
    mp3 = models.FilePathField(path="/media/", blank=True, null=True)   #as per MEDIA_URL in settings.py

    def __unicode__(self):
        short_text = truncatesmart(self.text, 50)
        return '%s' % short_text   

    def get_absolute_url(self):
        url = reverse('paragraphs', kwargs={'grade_level': reading.unit.grade.level, 'unit_slug': reading.unit.slug, 'reading_slug':reading.slug })
        return "%s" % url





#Alternate model below. Might it be simpler just to have everything in one table? 
#Or will that impact efficiency?
"""
class Alternate(models.Model):
    grade = models.CharField(max_length=10)
    unit_name = models.CharField(max_length=50)
    reading_title = models.CharField(max_length=100)
    passage_text = models.CharField(max_length=1000)        #each paragraph has multiple passages...           
    passage_num = models.CharField(max_length=20)           #indicates individual passage...
    mp3 = models.FilePathField(path="/media/")

    def __str__(self):
        return self.reading_title, self.passage_num
"""