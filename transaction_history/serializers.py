from rest_framework import serializers

from transaction_history.models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer[TransactionHistory]):
    class Meta:
        model: type[TransactionHistory] = TransactionHistory
        fields: list[str] = [
            "id",
            "account",
            "transaction_amount",
            "transaction_type",
            "balance_after_transaction",
            "deposit_withdrawal_type",
            "transaction_description",
            "transaction_date",
            "transaction_time",
        ]
