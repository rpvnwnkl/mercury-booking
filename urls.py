from django.conf.urls.defaults import *
from settings import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mercury_booking/', include('mercury_booking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('booking.urls')),

    url(r'^rosetta/', include('rosetta.urls')),

    (r'^mb_b_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': APPLICATION_ROOT + 'mb_media/'}),
)
