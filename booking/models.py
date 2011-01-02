from django.db import models
from entity.models import *

WEEK_DAYS = (
	(1,'Lunedi`'),
	(2,'Martedi`'),
	(3,'Mercoledi`'),
	(4, 'Giovedi`'),
	(5,'Venerdi`'),
	(6,'Sabato'),
	(7,'Domenica'),
	)

class Period(models.Model):
    playzone = models.ForeignKey(PlayZone)
    title = models.CharField(max_length=255)
    description = models.TextField(default = '',null=True,blank=True)
    date_start = models.DateField()
    date_end = models.DateField()

    def __unicode__(self):
    	return '%s' % self.title

class Week(models.Model):
	period = models.ForeignKey(Period)
	description = models.TextField(null=True,blank=True,default='')
   	day_start = models.IntegerField(choices=WEEK_DAYS)
   	day_end = models.IntegerField(choices=WEEK_DAYS)
   	time_start = models.TimeField()
   	time_end = models.TimeField()
   	slot = models.TimeField(default='',blank=True,null=True)
   	
   	def __unicode__(self):
   		return '%s --- %s ' % (self.time_start,self.time_end)

class Booking(models.Model):
   	week = models.ForeignKey(Week)
   	day_week = models.IntegerField(choices=WEEK_DAYS)
   	hour_start = models.TimeField()
   	hour_end = models.TimeField()
