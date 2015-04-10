from django.contrib import admin
from .models import Registry

class RegistryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Registry,RegistryAdmin)