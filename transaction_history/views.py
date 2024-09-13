from typing import Any, Optional

from rest_framework import status, viewsets
from rest_framework.response import Response

from transaction_history.models import TransactionHistory
from transaction_history.serializers import TransactionHistorySerializer


class TransactionHistoryViewSet(viewsets.ModelViewSet[TransactionHistory]):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request: Any, pk: Optional[str] = None) -> Response:
        transaction: TransactionHistory = self.get_object()
        serializer = self.get_serializer(transaction)
        return Response(serializer.data)

    def destroy(self, request: Any, pk: Optional[str] = None) -> Response:
        transaction: TransactionHistory = self.get_object()
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
