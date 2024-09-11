from typing import Any

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class SocialChoices(models.TextChoices):
        COMMON = "common", "Common"
        KAKAO = "kakao", "Kakao"
        NAVER = "naver", "Naver"
        GOOGLE = "google", "Google"

    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, null=True, blank=True, unique=False)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, unique=True, null=True)

    social_type = models.CharField(
        max_length=20,
        choices=SocialChoices.choices,
        default=SocialChoices.COMMON,
    )

    email_is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
