from django.db import models

class Proprety(models.Model):
    id = models.AutoField(primary_key=True)
    adresse = models.CharField(max_length=31)
    description = models.CharField(max_length=31)
    size = models.FloatField(editable=False, null=True)


    def __str__(self):
        return f"{self.size} iri mu  {self.adresse} avec {self.description} "
    
class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.type_name}"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    property_list = models.ForeignKey(Proprety,on_delete=models.CASCADE)
    prix = models.FloatField()
    listing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property_list} {self.prix} le {self.listing_date} "
    
class RentalUnity(models.Model):
    id = models.AutoField(primary_key=True)
    property_unit = models.ForeignKey(Proprety,on_delete=models.CASCADE)
    unit_number = models.FloatField()                                     #enregister les informations specifiques à chaque unité de location disponible dans une proprieté
    monthly_rent = models.FloatField() # montant du loyer msensuel  pour  une unité de location   
    def __str__(self):
        return f"{self.unit_number} se loue {self.monthly_rent}"
    
class Tenant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=31)
    adresse = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=31)
    def __str__(self):
        return f"{self.name} {self.adresse} {self.phone_number}"

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
    payment_unit= models.ForeignKey(RentalUnity,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.payment_date} {self.amount}"


class Invoice(models.Model):
    id =  models.AutoField(primary_key=True)
    tenant_invoice = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    unit_invoice =models.ForeignKey(RentalUnity,on_delete=models.CASCADE) 
    invoice_date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=31)
    def __str__(self):
        return f"{self.invoice_date} {self.amount}"


# Create your models here.
