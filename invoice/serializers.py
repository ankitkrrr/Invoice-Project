from rest_framework import serializers
from .models import Items,Invoice



class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField('item_name')
    quantity = serializers.SerializerMethodField('quantity')
    price = serializers.SerializerMethodField('price')
    tax = serializers.SerializerMethodField('tax')
    class Meta:
        model = Invoice
        fields = [
            'seller_name',
            'seller_phone',
            'seller_address',
            'buyer_name',
            'buyer_phone',
            'buyer_address',
            'item_name',
            'quantity',
            'price',
            'tax'
        ]