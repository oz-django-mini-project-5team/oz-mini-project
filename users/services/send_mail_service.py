from abc import abstractmethod
from typing import Optional, Union

from django.conf import settings
from django.core import signing
from django.core.mail import send_mail
from django.core.signing import SignatureExpired, TimestampSigner
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from users.models import User


class EmailService:
    def __init__(self, user: User, request: Request) -> None:
        self.user = user
        self.request = request
        self.email_from = settings.EMAIL_HOST_USER
        self.recipient_list = [user.email]

    def signer(self) -> str:
        signer = TimestampSigner()
        signed_user_email = signer.sign(self.user.email)
        signer_dump = signing.dumps(signed_user_email)
        return signer_dump

    def get_url(self, uri: str) -> str:
        link = f"/api/v1/users/{uri}/?code={self.signer()}"
        return f"{self.request.scheme}://{self.request.get_host()}{link}"

    def send_email(self, subject: str, message: str) -> None:
        send_mail(subject, message, self.email_from, self.recipient_list)

    def send_register_mail(self) -> None:
        uri = "active"
        activation_url = self.get_url(uri)

        subject = "Confirm your Account"
        message = f"Hi {self.user.name},\n\n" f"Please click the link below to confirm your account:\n{activation_url}"

        self.send_email(subject, message)


class CommonDecodeSignerUser:
    """
    sign해서 보낸 이메일 인증 url을 decoding 하는 클래스
    """

    def __init__(self) -> None:
        self.code: Optional[str] = None
        self.signer: Optional[TimestampSigner] = None
        self.user: Optional[User] = None

    def decode_signer(self, request: Request) -> Union[str, Response, None]:
        self.code = request.GET.get("code", "")
        self.signer = TimestampSigner()
        try:
            decoded_user_email = signing.loads(self.code)
            email = self.signer.unsign(decoded_user_email, max_age=60 * 3)
            self.user = User.objects.get(email=email)

        except SignatureExpired:
            return Response({"error": "expired time"}, status=status.HTTP_400_BAD_REQUEST)

        return self.handle_save_user(request)

    @abstractmethod
    def handle_save_user(self, request: Request) -> Response:
        pass
