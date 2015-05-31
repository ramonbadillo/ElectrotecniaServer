from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timeStampClient","idKill","kwh"]
    class Meta:
        model = Record



admin.site.register(Record,RecordAdmin)
