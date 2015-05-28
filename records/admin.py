from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record,RecordAdmin)
