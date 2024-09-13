from typing import Any, Optional

from rest_framework import status, viewsets
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet[Account]):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request: Any, pk: Optional[str] = None) -> Response:
        account: Account = self.get_object()
        serializer = self.get_serializer(account)
        return Response(serializer.data)

    def update(self, request: Any, pk: Optional[str] = None) -> Response:
        account: Account = self.get_object()
        serializer = self.get_serializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request: Any, pk: Optional[str] = None) -> Response:
        account: Account = self.get_object()
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
