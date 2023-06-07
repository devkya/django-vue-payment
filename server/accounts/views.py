from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
class SignupAPIView(APIView):
    # TODO: User 모델 생성(form or serializer)
    model = User
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "user": serializer.data,
            },
            status=201,
        )


class LoginAPIView(APIView):
    pass


class LogoutAPIView(APIView):
    pass


class ProfileAPIView(APIView):
    pass
