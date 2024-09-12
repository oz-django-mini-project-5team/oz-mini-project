from typing import Any, Dict

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserLoginSerializer(serializers.Serializer[User]):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise NotFound(detail={"email": "User not found."})

        if not user.check_password(password):
            raise AuthenticationFailed(detail={"password": "Incorrect password."})

        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data_with_token = {
            "user": {"id": user.id, "email": user.email, "name": user.name},
            "refresh_token": refresh_token,
            "access_token": access_token,
        }

        return data_with_token


# mypy: ignore-errors
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["name"] = user.name

        return token
