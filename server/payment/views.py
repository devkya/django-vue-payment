from rest_framework.views import APIView
from .serializers import PaymentSerializer
from rest_framework.response import Response


# Create your views here.
class PaymentNewAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pk = serializer.validated_data.get("id")
        test = {"a": 1, "b": 2}
        return Response(serializer.data, status=201)


class PaymentPayAPIView(APIView):
    pass
