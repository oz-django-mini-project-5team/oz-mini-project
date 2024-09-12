from django.test import TestCase

from accounts.models import Account
from users.models import User


class TestCreateAccount(TestCase):

    def test_create_account(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234!")
        account = Account.objects.create(
            user_id=user.pk,
            account_type="savings",
            account_number="1234567812345678",
            bank_code="kakao",
        )

        self.assertEqual(user.pk, account.user_id)
