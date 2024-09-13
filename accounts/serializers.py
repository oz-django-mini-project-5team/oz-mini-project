from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer[Account]):  # 제네릭 타입 추가
    account_number: serializers.SerializerMethodField = serializers.SerializerMethodField()  # 타입 파라미터 제거

    class Meta:
        model: type[Account] = Account
        fields: list[str] = ["user", "account_number", "bank_code", "account_type", "balance"]

    def get_account_number(self, obj: Account) -> str:
        # 계좌 번호 마지막 4자리 마스킹
        return obj.account_number[:-4] + "****"


class AccountCreateSerializer(serializers.ModelSerializer[Account]):  # 제네릭 타입 추가
    class Meta:
        model: type[Account] = Account
        fields: list[str] = ["user", "account_number", "bank_code", "account_type", "balance"]
