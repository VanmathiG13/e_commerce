from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include the full category object with its serializer

    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_name',
            'description',
            'category',  # This will now include the category name and ID
            'image_url',
            'mrp',
            'discounted_price',
            'product_count'
        ]
