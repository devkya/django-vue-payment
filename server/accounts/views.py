from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
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
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {
                    "error": "Please provide both username and password",
                },
                status=400,
            )
        # 로그인 정보만 확인
        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {
                    "error": "Invalid Credentials",
                },
                status=400,
            )
        # 사용자 객체를 가져와 쿠기 설정
        login(request, user)
        return Response(
            {
                "user": UserSerializer(user).data,
            },
            status=200,
        )


class LogoutAPIView(APIView):
    pass


class ProfileAPIView(APIView):
    pass
