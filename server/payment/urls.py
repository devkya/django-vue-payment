from django.urls import path, include
from .views import PaymentNewAPIView, PaymentDetailAPIView, PaymentCheckAPIView

urlpatterns = [
    path("new/", PaymentNewAPIView.as_view(), name="payment-new"),
    path("<int:pk>/", PaymentDetailAPIView.as_view(), name="payment-pay"),
    path("<int:pk>/check/", PaymentCheckAPIView.as_view(), name="payment-check"),
]
