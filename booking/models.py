from django.db import models
from entity.models import *
from django.utils.translation import ugettext as _

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
    playzone = models.ForeignKey(PlayZone, related_name=_('playzone'))
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('title'), default = '', null=True, blank=True)
    date_start = models.DateField(_('date start'))
    date_end = models.DateField(_('date end'))

    def __unicode__(self):
    	return '%s' % self.title

class Week(models.Model):
	period = models.ForeignKey(Period, related_name=_('period'))
	description = models.TextField(_('description'), null=True, blank=True, default='')
   	day_start = models.IntegerField(_('start day'), choices=WEEK_DAYS)
   	day_end = models.IntegerField(_('end day'), choices=WEEK_DAYS)
   	time_start = models.TimeField(_('start time'))
   	time_end = models.TimeField(_('end time'))
   	slot = models.TimeField(_('slot'), default='',blank=True,null=True)
   	
   	def __unicode__(self):
   		return '%s --- %s ' % (self.time_start,self.time_end)

class Booking(models.Model):
   	week = models.ForeignKey(Week, related_name=_('week'))
   	day_week = models.IntegerField(_('title'), choices=WEEK_DAYS)
   	hour_start = models.TimeField(_('start hour'))
   	hour_end = models.TimeField(_('end hour'))
