from rest_framework import serializers

from transaction_history.models import TransactionHistory


class DepositWithdrawalSerializer(serializers.Serializer):  # type: ignore
    amount = serializers.IntegerField()
    d_w_type = serializers.ChoiceField(choices=TransactionHistory.DepositWithdrawalTypeChoices)
    transaction_type = serializers.ChoiceField(choices=TransactionHistory.TransactionTypeChoices)
    account_id = serializers.CharField()


class TransactionHistorySerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = TransactionHistory
        fields = "__all__"
