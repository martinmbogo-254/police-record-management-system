from django.contrib import admin
from.models import Arrest, Report,Crime
# Register your models here.
admin.site.register(Crime)
admin.site.register(Arrest)
admin.site.register(Report)