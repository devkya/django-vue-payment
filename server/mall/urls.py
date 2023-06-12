from django.urls import path, include
from .views import ProductViewSet, AddCartAPIView, CartAPIView
from rest_framework.routers import DefaultRouter

product_router = DefaultRouter()
product_router.register("products", ProductViewSet, basename="product")


urlpatterns = [
    path("", include(product_router.urls)),
    path("add-cart/<int:product_pk>/", AddCartAPIView.as_view(), name="add-cart"),
    path("cart/", CartAPIView.as_view(), name="cart"),
]
