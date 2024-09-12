from typing import Any

from django.contrib.auth import login
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers.jwt_serializer import UserLoginSerializer
from users.serializers.user_serializer import UserRegisterSerializer
from users.services.create_user_service import CreateUserService
from users.services.send_mail_service import (CommonDecodeSignerUser,
                                              EmailService)


class UserRegisterAPIView(GenericAPIView[User]):

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        user = CreateUserService.create_user(validated_data)

        email_service = EmailService(user, request)
        email_service.send_register_mail()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ActivateUser(CommonDecodeSignerUser, APIView):

    permission_classes = (AllowAny,)

    def get(self, request: Any) -> str | Response | None:
        return self.decode_signer(request)

    def handle_save_user(self, request: Any) -> Response:
        if self.user is not None:
            self.user.is_active = True
            self.user.email_is_verified = True
            self.user.save()
            return Response({"message": "Account activated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Any) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        access_token = data["access_token"]
        refresh_token = data["refresh_token"]

        response = Response(
            {
                "user": data["user"]["email"],
                "message": "login success",
                "jwt_token": {"access_token": access_token, "refresh_token": refresh_token},
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie("access_token", access_token, httponly=True)
        response.set_cookie("refresh_token", refresh_token, httponly=True)

        return response


class UserLogoutAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Any) -> Response:
        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

        # 쿠키에서 access_token과 refresh_token을 삭제
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
