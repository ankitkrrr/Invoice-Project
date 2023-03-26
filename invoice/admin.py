from django.contrib import admin
from .models import  Items, Invoice
# Register your models here.


    
@admin.register(Items)
class ItemsModelAdmin(admin.ModelAdmin):
    list_display=['id','invoice_id','item_name','quantity','tax','price']

@admin.register(Invoice)
class InvoiceModelAdmin(admin.ModelAdmin):
    list_display=['id','seller_name','seller_phone','seller_address','buyer_name','buyer_phone','buyer_address']
    

    
    
    

    