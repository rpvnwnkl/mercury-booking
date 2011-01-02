from booking.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext

from booking import *

def period_insert(request):
	period_form = PeriodForm()
	if request.method=='POST':
		period_form = PeriodForm(request.POST)
		if period_form.is_valid():
			#period = Period(instance = request.POST)
			#print period
			period_form.save()
			return render_to_response('base.html', {'var1':'Periodo salvato correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':period_form,'form_title':'Inserimento periodo'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':period_form,'form_title':'Inserimento periodo'},context_instance=RequestContext(request))

def period_list(request):
	periods = Period.objects.all()
	return render_to_response('booking/period/list.html', {'periods':periods})

def period_delete(request,id):
	try:
		period = Period.objects.get(pk=id)
		period.delete()
	except:
		return render_to_response('base.html', {'var1':'Errore nella cancellazone del periodo!'})
		pass	
	return render_to_response('base.html', {'var1':'Periodo cancellato con successo!'})

def period_edit(request,period_id):
	period = Period.objects.get(pk=period_id)
	period_form = PeriodForm(instance=period)
	if request.method=='POST':
		period_form = PeriodForm(request.POST,instance=period)
		if period_form.is_valid():
			period_form.save()
			return render_to_response('base.html', {'var1':'Periodo salvato correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':period_form,'form_title':'Modifica periodo'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':period_form,'form_title':'Modifica periodo'},context_instance=RequestContext(request))

def week_insert(request):
	week_form = WeekForm()
	if request.method=='POST':
		week_form = WeekForm(request.POST)
		if week_form.is_valid():
			#period = Period(instance = request.POST)
			#print period
			week_form.save()
			return render_to_response('base.html', {'var1':'Gestione salvata correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':week_form,'form_title':'Gestione settimana'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':week_form,'form_title':'Gestione settimana'},context_instance=RequestContext(request))


def week_edit(request,week_id):
	week = Week.objects.get(pk=week_id)
	week_form = WeekForm(instance=week)
	if request.method=='POST':
		week_form = WeekForm(request.POST,instance=week)
		if week_form.is_valid():
			week_form.save()
			return render_to_response('base.html', {'var1':'Dati della settimana salvati correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':week_form,'form_title':'Gestione settimana'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':week_form,'form_title':'Gestione settimana'},context_instance=RequestContext(request))

def week_list(request):
	periods = Period.objects.all()
	return render_to_response('booking/week/list.html', {'periods':periods,'form_title':'Lista orari settimanali per periodi'},context_instance=RequestContext(request))


def week_delete(request,id):
	try:
		week = Week.objects.get(pk=id)
		week.delete()
	except:
		return render_to_response('base.html', {'var1':'Errore nella cancellazione della gestione settimanale!'})
		pass	
	return render_to_response('base.html', {'var1':'Gestione settimanale cancellata con successo!'})


def booking_insert(request):
	booking_form = BookingForm()
	if request.method=='POST':
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			#period = Period(instance = request.POST)
			#print period
			booking_form.save()
			return render_to_response('base.html', {'var1':'Prenotazione salvata correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':booking_form,'form_title':'Prenotazioni'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':booking_form,'form_title':'Prenotazioni'},context_instance=RequestContext(request))


def booking_list(request):
	booking = Booking.objects.all().order_by('week')
	return render_to_response('booking/booking/list.html', {'booking':booking,'form_title':'Lista prenotazioni'},context_instance=RequestContext(request))

def booking_delete(request,id):
	try:
		booking = Booking.objects.get(pk=id)
		booking.delete()
	except:
		return render_to_response('base.html', {'var1':'Errore nella cancellazione della prenotazione!'})
		pass	
	return render_to_response('base.html', {'var1':'Prenotazione cancellata con successo!'})

def booking_edit(request,booking_id):
	booking = Booking.objects.get(pk=booking_id)
	booking_form = BookingForm(instance=booking)
	if request.method=='POST':
		booking_form = BookingForm(request.POST,instance=booking)
		if booking_form.is_valid():
			booking_form.save()
			return render_to_response('base.html', {'var1':'Prenotazione salvato correttamente'},context_instance=RequestContext(request))
		else:
			return render_to_response('booking/manage.html', {'form':booking_form,'form_title':'Modifica prenotazione'},context_instance=RequestContext(request))	
	return render_to_response('booking/manage.html', {'form':booking_form,'form_title':'Modifica prenotazione'},context_instance=RequestContext(request))
