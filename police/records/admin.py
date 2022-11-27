from django.contrib import admin
from.models import Arrest, Report,Crime


class ArrestAdmin(admin.ModelAdmin):
    list_display =('arrest_id','suspect_name','suspect_id','crime_type','crime_location','description')
    search_fields = ['arrest_id','suspect_name','suspect_id', 'date']


class ReportAdmin(admin.ModelAdmin):
    list_display =('report_id','victim_name','victim_id','crime_type','crime_location','description')
    search_fields = ['report_id','victim_name','victim_id', 'date']

# Register your models here.
admin.site.register(Crime)
admin.site.register(Arrest,ArrestAdmin)
admin.site.register(Report,ReportAdmin)

admin.site.site_header = "POLICE RECORDS ADMINISTRATION"