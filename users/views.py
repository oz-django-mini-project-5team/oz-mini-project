from typing import Any

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserRegisterSerializer
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
