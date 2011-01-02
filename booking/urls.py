from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^admin/period/insert/$', 'booking.views.period_insert', name='insert_period'),
    url(r'^admin/period/list/$', 'booking.views.period_list', name='list_period'),
    url(r'^admin/period/edit/(\d+)/$', 'booking.views.period_edit', name='edit_period'),
    url(r'^admin/period/delete/(\d+)/$', 'booking.views.period_delete', name='delete_period'),
    
    
    url(r'^admin/week/insert/$', 'booking.views.week_insert', name='insert_week'),
    url(r'^admin/week/list/$', 'booking.views.week_list', name='list_week'),
    url(r'^admin/week/edit/(\d+)/$', 'booking.views.week_edit', name='edit_week'),
    url(r'^admin/week/delete/(\d+)/$', 'booking.views.week_delete', name='delete_week'),
    
    
    url(r'^admin/booking/insert/$', 'booking.views.booking_insert', name='insert_booking'),
    url(r'^admin/booking/list/$', 'booking.views.booking_list', name='list_booking'),
    url(r'^admin/booking/delete/(\d+)/$', 'booking.views.booking_delete', name='delete_booking'),
    url(r'^admin/booking/edit/(\d+)/$', 'booking.views.booking_edit', name='edit_booking'),
)
