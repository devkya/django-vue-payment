from rest_framework.serializers import ModelSerializer
from .models import Product, Category, CartProduct
from rest_framework import serializers
from accounts.serializers import UserSerializer


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


class CartProductSerializer(ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id", "product", "quantity", "user", "product"]


class CarCartProductSerializer(ModelSerializer):
    user = UserSerializer()
    product = ProductListSerializer()

    class Meta:
        model = CartProduct
        fields = ["id", "product", "quantity", "user", "product"]
