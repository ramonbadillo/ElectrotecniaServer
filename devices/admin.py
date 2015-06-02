from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","modelo","avarage"]
    class Meta:
        model = Device

admin.site.register(Device,DeviceAdmin)
