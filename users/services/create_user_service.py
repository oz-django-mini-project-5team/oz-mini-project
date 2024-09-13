from typing import Any, Dict

from rest_framework.exceptions import ValidationError

from users.models import User


class CreateUserService:

    @staticmethod
    def create_user(validated_data: Dict[str, Any]) -> User:
        try:
            user = User.objects.create(**validated_data)
            user.set_password(validated_data["password"])
            user.save()

            return user

        except ValueError:
            raise ValidationError("잘못된 값을 입력 받았습니다.")
