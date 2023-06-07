from rest_framework.serializers import ModelSerializer
from .models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "merchant_uid", "name", "amount", "status", "is_paid_ok"]
