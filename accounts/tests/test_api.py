from django.test import TestCase

from accounts.models import Account
from users.models import User


class AccountTest(TestCase):

    def test_create_account(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234!")
        account = Account.objects.create(
            user_id=user.id,
            bank_code="kakao",
            account_number="1234567890",
            account_type="savings",
            balance=1000,
        )

        self.assertEqual(user.id, account.user_id)

    def test_delete_account(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234!")
        account = Account.objects.create(
            user_id=user.id,
            bank_code="kakao",
            account_number="1234567890",
            account_type="savings",
            balance=1000,
        )

        self.assertEqual(user.id, account.user_id)

        account.delete()

        self.assertEqual(Account.objects.count(), 0)

    def test_update_account(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234!")
        account = Account.objects.create(
            user_id=user.id,
            bank_code="kakao",
            account_number="1234567890",
            account_type="savings",
            balance=1000,
        )

        self.assertEqual(user.id, account.user_id)

        account.balance = 200
        account.save()

        self.assertEqual(account.balance, 200)
