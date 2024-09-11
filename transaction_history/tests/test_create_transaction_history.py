from django.test import TestCase

from accounts.models import Account
from transaction_history.models import TransactionHistory
from users.models import User


class TestCreateTransactionHistory(TestCase):

    def test_create_transaction_history(self) -> None:
        user = User.objects.create_user(email="test@test.com", password="Qwer1234!")
        account = Account.objects.create(
            user_id=user.pk,
            account_type="savings",
            account_number="1234567812345678",
            bank_code="kakao",
            balance=2000,
        )
        transaction_history1 = TransactionHistory.objects.create(
            account_id=account.pk,
            transaction_amount=1000,
            transaction_type="cash",
            balance_after_transaction=account.balance + 1000,
            deposit_withdrawal_type="deposit",
            transaction_description="ATM 경기 북부",
        )

        self.assertEqual(transaction_history1.account_id, account.pk)
