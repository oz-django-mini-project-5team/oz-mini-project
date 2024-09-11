from django.db import models

from users.models import User


class Account(models.Model):
    class BankCodes(models.TextChoices):
        KAKAO = "kakao", "Kakao Bank"
        KB = "kb", "KB Kookmin Bank"
        NH = "nh", "NH NongHyup Bank"
        IBK = "ibk", "IBK Industrial Bank of Korea"

    class AccountTypes(models.TextChoices):
        SAVINGS = "savings", "Savings Account"
        CHECKING = "checking", "Checking Account"
        OVERDRAFT = "overdraft", "Overdraft Account"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=16, unique=True)
    bank_code = models.CharField(max_length=10, choices=BankCodes.choices)
    account_type = models.CharField(max_length=20, choices=AccountTypes.choices)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)
