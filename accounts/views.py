from typing import Optional, Type

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Account
from .serializers import AccountCreateSerializer, AccountSerializer


class AccountViewSet(ModelViewSet[Account]):  # 제네릭 타입 추가
    queryset = Account.objects.all()

    def get_serializer_class(self) -> Type[BaseSerializer[Account]]:  # BaseSerializer에 제네릭 추가
        """생성 시 AccountCreateSerializer, 조회 시 AccountSerializer 사용"""
        if self.action == "create":
            return AccountCreateSerializer
        return AccountSerializer

    @action(detail=True, methods=["delete"], url_path="delete")
    def delete_account(self, request: Request, pk: Optional[str] = None) -> Response:  # Optional[str] 추가
        """계좌 삭제 기능"""
        account: Account = self.get_object()
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
