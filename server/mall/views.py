from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("pages", self.page.paginator.num_pages),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category")
    serializer_class = ProductListSerializer
    pagination_class = StandardResultsSetPagination
