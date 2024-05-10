from django.db import models
from django.contrib.auth.models import User


class Proprety(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31, default=0)
    property_number = models.CharField(max_length=31, default=0)
    list = models.FloatField(editable=False, null=True)
    adresse = models.CharField(max_length=31)
    description = models.CharField(max_length=31)
    size = models.FloatField(editable=False, null=True)
    prix = models.FloatField(default=0)


    def __str__(self):
        return f"{self.nom} {self.property_number} se loue  {self.prix}"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, default=0)
    property_name = models.ForeignKey(Proprety,on_delete=models.CASCADE)
    list_initiale = models.FloatField(default=0)
    list_actuelle = models.FloatField(editable=False, null=True,default=0)
    prix = models.FloatField(default=0)
    listing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property_name} {self.prix} le {self.listing_date} "
    
class Tenant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=31)
    adresse = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=31)
    def __str__(self):
        return f"{self.name} {self.adresse} {self.phone_number}"
class Demande(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    prix_total = models.FloatField(editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=63, null=True)
    done = models.BooleanField(default=False, editable=False)

    def __str__(self) -> str:
        return f"Demande de {self.created_by} valant {self.prix_total}"
class DemandeLocation(models.Model):
   id = models.BigAutoField(primary_key=True)
   property_name = models.ForeignKey(Proprety, on_delete=models.PROTECT)
   demande = models.ForeignKey(Demande, on_delete=models.CASCADE, editable=False)
   list = models.FloatField()

   def __str__(self) -> str:
        return f"Demande de location de {self.list} {self.property_name.property_number}"

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    tenant_contract = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    deposit_amount = models.FloatField()
    def __str__(self):
        return f"{self.start_date} {self.end_date} {self.deposit_amount}"
    
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    payment_tenant= models.ForeignKey(Tenant,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.payment_date} {self.amount}"


class Invoice(models.Model):
    id =  models.AutoField(primary_key=True)
    tenant_invoice = models.ForeignKey(Tenant,on_delete=models.CASCADE) 
    invoice_date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=31)
    def __str__(self):
        return f"{self.invoice_date} {self.amount}"


# Create your models here.
