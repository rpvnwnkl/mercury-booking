from django.contrib import admin
from mercury_booking.entity.models import *

class StaticVisualizationAdmin(admin.ModelAdmin):
    list_filter = ('kindzone',)

admin.site.register(KindZone)
admin.site.register(ZoneParameter)
admin.site.register(StaticVisualization,StaticVisualizationAdmin)
admin.site.register(Entity)
admin.site.register(PlayZone)
