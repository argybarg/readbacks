from django.db import models

class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s' % self.grade

    #class Admin: pass


class Unit(models.Model):
    grade = models.ForeignKey(Grade)
    unit = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.unit

    #class Admin: pass


class Reading(models.Model):
    unit = models.ForeignKey(Unit)
    reading = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.reading

    #class Admin: pass


class Paragraph(models.Model):
    reading = models.ForeignKey(Reading)
    paragraph = models.CharField(max_length=1000)                  
    mp3 = models.FilePathField(path="/media/", blank=True, null=True)              #as per MEDIA_URL in settings.py

    def __unicode__(self):
        return '%s' % self.paragraph                            #  truncate later?  maybe id number would be better? subl won't let me do that!!

    #class Admin: pass



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