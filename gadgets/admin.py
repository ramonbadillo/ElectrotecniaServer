from django.contrib import admin
from .models import Gadget

class GadgetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gadget,GadgetAdmin)