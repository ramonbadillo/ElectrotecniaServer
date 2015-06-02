from django.contrib import admin
from .models import Gadget

class GadgetAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","idKill","idDev"]
    class Meta:
        model = Gadget

admin.site.register(Gadget,GadgetAdmin)
