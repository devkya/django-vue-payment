from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product, Category
from .serializers import ProductListSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get(self, request):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
