from django.contrib import admin
from .models import *


admin.site.register(Proprety)
admin.site.register(PropertyType)
admin.site.register(Listing)
admin.site.register(RentalUnity)
admin.site.register(Tenant)
admin.site.register(Contract)
admin.site.register(Invoice)

# Register your models here.
