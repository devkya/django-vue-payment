from rest_framework.serializers import ModelSerializer
from .models import Product, Category
from rest_framework import serializers


class ProductListSerializer(ModelSerializer):
    category_name = serializers.CharField(source="category.name")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category_name",
            "status",
            "photo",
            "created_at",
            "updated_at",
        ]
