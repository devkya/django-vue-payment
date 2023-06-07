from django.conf import settings
from django.http import JsonResponse
from iamport import Iamport
from rest_framework.views import APIView
from .serializers import PaymentSerializer
from rest_framework.response import Response
from .models import Payment


# Create your views here.
class PaymentNewAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


class PaymentDetailAPIView(APIView):
    def get(self, request, pk):
        instance = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(instance)
        print(serializer.data)
        return JsonResponse(serializer.data, status=200)


class PaymentCheckAPIView(APIView):
    def get(self, request, pk):
        payment = Payment.objects.get(id=pk)
        meta = payment.portone_check(commit=True)
        return JsonResponse(meta, status=200)
