from django.forms import ModelForm
from booking.models import *
from django import forms

from models import *

valid_time_format = ["%H:%M","%H:%M:%S","%H"]

class PeriodForm(ModelForm):
    class Meta:
            model = Period
            
    def clean(self):
        cd = self.cleaned_data
        cd_iv = super(PeriodForm, self).is_valid()
        if not cd_iv:
            return cd
        from django.core.exceptions import ValidationError
        if cd.get('date_start') > cd.get('date_end'):
        	raise ValidationError("Data inizio periodo maggiore della data di fine periodo!")
	return cd
        
class WeekForm(ModelForm):
    
    time_start = forms.TimeField(input_formats=valid_time_format)
    time_end = forms.TimeField(input_formats=valid_time_format)
    slot = forms.TimeField(input_formats=valid_time_format)
    
    class Meta:
            model = Week
            
    def clean(self):
        import time
        cd = self.cleaned_data
        cd_iv = super(WeekForm, self).is_valid()
        if not cd_iv:
            return cd
        from django.core.exceptions import ValidationError
        if cd.get('day_start') > cd.get('day_end'):
            raise ValidationError("Giorno inizio settimana maggiore del giorno di fine settimana!")
        if cd.get('time_start') > cd.get('time_end'):
            raise ValidationError("Orario inizio maggiore dell'orario di fine!")
        import datetime
        t_s = datetime.timedelta(hours=int(str(cd.get('time_start')).split(':')[0]),seconds=int(str(cd.get('time_start')).split(':')[1]))
        t_e = datetime.timedelta(hours=int(str(cd.get('time_end')).split(':')[0]),seconds=int(str(cd.get('time_end')).split(':')[1]))
        if cd.get('slot'):
            slot = datetime.timedelta(hours=int(str(cd.get('slot')).split(':')[0]),seconds=int(str(cd.get('slot')).split(':')[1]))
            if (t_e-t_s) < slot and slot is not None:
                raise ValidationError("Minimo di tempo prenotazione maggiore della disponibilita` totale!")
        return cd        
            
class BookingForm(ModelForm):
    hour_start = forms.TimeField(input_formats=valid_time_format)
    hour_end = forms.TimeField(input_formats=valid_time_format)
    day_week = models.IntegerField(choices=WEEK_DAYS)
    
    class Meta:
        model = Booking            

        
            
