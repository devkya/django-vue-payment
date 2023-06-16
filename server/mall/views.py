from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Product, Category, CartProduct
from .serializers import (
    ProductListSerializer,
    CartProductSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from accounts.models import User
from django.shortcuts import get_object_or_404


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
    queryset = Product.objects.filter(status=Product.Status.ACTIVE).select_related(
        "category"
    )
    serializer_class = ProductListSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        search = request.query_params.get("search", None)

        if search:
            queryset = queryset.filter(name__icontains=search)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AddCartAPIView(APIView):
    def post(self, request, product_pk):
        try:
            queryset = CartProduct.objects.all()
            user = User.objects.get(username=request.data["username"])
            product_queryset = Product.objects.filter(status=Product.Status.ACTIVE)
            product = get_object_or_404(product_queryset, pk=product_pk)

            cart_product, is_created = queryset.get_or_create(
                user=user,
                product=product,
                defaults={"quantity": int(request.data["quantity"])},
            )
            if not is_created:
                cart_product.quantity += int(request.data["quantity"])
                cart_product.save()
                return Response(status=status.HTTP_200_OK)

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CartAPIView(APIView):
    def get(self, request):
        queryset = CartProduct.objects.all()
        serializer = CartProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            user = User.objects.get(username=request.data["username"])
            queryset = CartProduct.objects.filter(user=user)
            serializer = CartProductSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
