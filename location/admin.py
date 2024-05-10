from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from .models import *

admin.site.site_header = "BUSINESS LOCATION"


@admin.register(Proprety)
class PropertyAdmin(admin.ModelAdmin):
    list_display = "nom","property_number","list","adresse", "description", "size","prix", "options"
    search_fields = "nom",

    def options(self, obj:Proprety):
        return mark_safe(f"<a href='/admin/location/listing/?property__id__exact={obj.id}'>voir listing</a>")

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display =  "created_by", "property_name", "listing_date",

    def save_model(self, request, obj: Listing, form, change) -> None:
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        property_name = obj.property_name
        try:
            property_name.list += obj.list_initiale
        except Exception:
            property_name.list = obj.list_initiale
        property_name.save()
        obj.list_actuelle = obj.list_initiale
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
    def delete_model(self, request, obj:Listing):
        property_name = obj.property_name
        property_name.list -= obj.list_actuelle
        property_name.save()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset: QuerySet[Listing]):
        for obj in queryset:
            property_name = obj.property_name
            property_name.list -= obj.list_actuelle
            property_name.save()
        return super().delete_queryset(request, queryset)
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = "name", "adresse", "phone_number",
@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin):
    list_display = "created_by", "prix_total", "created_at", "client","done"
@admin.register(DemandeLocation)
class DemandeLocationAdmin(admin.ModelAdmin):
    list_display = "property_name","demande","list"
    list_filter = "property_name",

    def save_model(self, request, obj:DemandeLocation, form, change):
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        property_name = obj.property_name
        if obj.list > (property_name.list or 0):
            messages.add_message(request, messages.ERROR, f"{property_name} hasigaye {property_name.list or 0} {property_name.property_number} gusa")
            return

        demande = Demande.objects.filter(done=False).first()
        if not demande:
            # demande = INSERT INTO Query(created_by) VALUES (request.user)
            demande = Demande.objects.create(created_by = request.user)
        obj.demande = demande
        obj.prix = obj.property_name.prix * obj.list
        demande.prix_total += obj.prix
        demande.save()
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj:DemandeLocation) -> None:
        demande = obj.demande
        demande.prix_total -= obj.prix
        demande.save()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset: QuerySet[DemandeLocation]) -> None:
        for obj in queryset:
            demande = obj.demande
            demande.prix_total -= obj.prix
            demande.save()
        return super().delete_queryset(request, queryset)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = "tenant_contract",  "start_date", "end_date","deposit_amount"
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = "payment_tenant", "payment_date", "amount"
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = "tenant_invoice", "invoice_date", "amount"

# Register your models here.
