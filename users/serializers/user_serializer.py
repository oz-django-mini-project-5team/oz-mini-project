from typing import Any, Dict

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserRegisterSerializer(ModelSerializer[User]):
    password2 = serializers.CharField(write_only=True, label="비밀번호 확인")

    class Meta:
        model = User
        fields = ["name", "email", "password", "password2"]

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        password = data.get("password")
        password2 = data.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match"})

        try:
            validate_password(password)
        except DjangoValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return data
