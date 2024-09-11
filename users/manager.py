from typing import TYPE_CHECKING, Any

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from users.models import User


class UserManager(BaseUserManager["User"]):

    use_in_migrations = True

    def create_user(self, email: str, password: str | None = None, **extra_fields: Any) -> "User":
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("email_is_verified", True)
        extra_fields.setdefault("name", "admin")

        return self.create_user(email, password, **extra_fields)
