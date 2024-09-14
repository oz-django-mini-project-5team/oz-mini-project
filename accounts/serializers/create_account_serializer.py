from rest_framework import serializers, status

from accounts.models import Account


class CreateAccountSerializer(serializers.ModelSerializer):  # type: ignore

    class Meta:
        model = Account
        fields = ("bank_code", "account_number", "account_type", "balance")
        read_only_fields = ("user",)

    def validate(self, data):  # type: ignore
        return data
