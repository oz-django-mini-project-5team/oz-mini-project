from typing import Optional

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import TransactionHistory
from .serializers import TransactionHistorySerializer


class TransactionHistoryViewSet(ModelViewSet[TransactionHistory]):  # 제네릭 타입 추가
    queryset = TransactionHistory.objects.all()
    serializer_class: type[TransactionHistorySerializer] = TransactionHistorySerializer

    @action(detail=True, methods=["delete"], url_path="delete")
    def delete_transaction(self, request: Request, pk: Optional[str] = None) -> Response:  # Optional[str] 추가
        """입출금 기록 삭제 기능"""
        transaction: TransactionHistory = self.get_object()
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
