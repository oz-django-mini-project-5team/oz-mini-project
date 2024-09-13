from typing import Any

from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer[Account]):
    class Meta:
        model: type[Account] = Account
        fields: list[str] = ["id", "user", "account_number", "bank_code", "account_type", "balance"]

    def update(self, instance: Account, validated_data: dict[str, Any]) -> Account:  # 제네릭 타입 추가
        instance.bank_code = validated_data.get("bank_code", instance.bank_code)
        instance.account_type = validated_data.get("account_type", instance.account_type)
        instance.balance = validated_data.get("balance", instance.balance)
        instance.save()
        return instance

