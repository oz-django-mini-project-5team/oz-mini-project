from typing import Union

from rest_framework import serializers

from .models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer[TransactionHistory]):
    class Meta:
        model: type[TransactionHistory] = TransactionHistory
        fields: Union[list[str], str] = "__all__"  # 리스트 또는 문자열을 허용
