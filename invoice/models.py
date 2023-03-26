
from django.db import models

# Create your models here.

class Invoice(models.Model):
    seller_name = models.CharField(max_length=255)
    seller_phone = models.CharField(max_length=255)
    seller_address = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=255)
    buyer_phone = models.CharField(max_length=255)
    buyer_address = models.CharField(max_length=255)
    invoice_date = models.DateTimeField()
    

    
class  Items(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    
    