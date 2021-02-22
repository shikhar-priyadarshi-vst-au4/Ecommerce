from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name', 'price', 'details', 'rating', 'discount', 'package_type', 'product_category')
        fields = '__all__'