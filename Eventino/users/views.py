from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAuthedUser
from users.serializers import UserSerializer
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

import jwt
import datetime


class registerAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found:)")

        if not user.check_password(password):
            raise AuthenticationFailed("Invalid password")

        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)

        response.data = {"jwt token": token}

        return response


class UserView(APIView):
    permission_classes = [IsAuthedUser]

    def get(self, request):
        user_id = jwt.decode(request.COOKIES.get("jwt"), "secret", algorithms="HS256")["id"]

        user = User.objects.filter(id=user_id).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthedUser]

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "successful"}

        return response
