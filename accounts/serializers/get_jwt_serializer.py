from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    InvalidToken,
    TokenError,
)

from accounts.models import Account
from users.models import User


class GetJwtSerializer(serializers.Serializer):  # type: ignore
    token = serializers.CharField()

    def validate(self, data) -> dict:  # type: ignore
        token = data.get("token")

        if not token:
            raise serializers.ValidationError({"detail": "토큰이 없어용!"})

        jwt_auth = JWTAuthentication()

        try:
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)

        except (InvalidToken, TokenError):
            raise serializers.ValidationError({"detail": "토큰이 유효하지 않아용!"})

        except AuthenticationFailed:
            raise serializers.ValidationError({"detail": "사용자 인증에 실패했어용!"})

        return {"user": user}


class AccountSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Account
        fields = "__all__"  # Adjust fields as needed
