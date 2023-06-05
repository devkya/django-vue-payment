from django.urls import path, include
from .views import PaymentNewAPIView

urlpatterns = [
    path("pay/", PaymentNewAPIView.as_view(), name="payment-new"),
]
