# type: ignore

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from accounts.serializers.create_account_serializer import CreateAccountSerializer
from accounts.serializers.deposit_withdrawal_serializer import (
    DepositWithdrawalSerializer,
    TransactionHistorySerializer,
)
from accounts.serializers.get_jwt_serializer import AccountSerializer, GetJwtSerializer
from transaction_history.models import TransactionHistory


class AccountAPIView(APIView):
    def get(self, request):
        token = request.COOKIES.get("access_token")

        serializer = GetJwtSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get("user")

        try:
            accounts = Account.objects.filter(user_id=user.id)
            accounts = AccountSerializer(accounts, many=True)
        except Account.DoesNotExist:
            return redirect("create/")

        return Response(accounts.data, status=status.HTTP_200_OK)


class AccountCreateAPIView(GenericAPIView):

    serializer_class = CreateAccountSerializer

    def post(self, request):
        # 유저 데이터 가져오기
        token = request.COOKIES.get("access_token")
        serializer = GetJwtSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")

        # 계좌 등록하기
        account_serializer = CreateAccountSerializer(data=request.data)
        account_serializer.is_valid(raise_exception=True)
        account = Account.objects.create(
            user_id=user.id,
            bank_code=account_serializer.validated_data.get("bank_code"),
            account_number=account_serializer.validated_data.get("account_number"),
            account_type=account_serializer.validated_data.get("account_type"),
            balance=account_serializer.validated_data.get("balance"),
        )

        # json화
        account = AccountSerializer(account)

        return Response(account.data, status=status.HTTP_201_CREATED)


class AccountUpdateAPIView(GenericAPIView):
    serializer_class = DepositWithdrawalSerializer

    def post(self, request):
        serializer = DepositWithdrawalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account_id = serializer.validated_data.get("account_id")
        amount = serializer.validated_data.get("amount")
        d_w_type = serializer.validated_data.get("d_w_type")
        account_balance = Account.objects.get(id=account_id).balance
        transaction_type = serializer.validated_data.get("transaction_type")

        if d_w_type == "deposit":
            transaction = TransactionHistory.objects.create(
                account_id=account_id,
                transaction_amount=amount,
                transaction_type=transaction_type,
                balance_after_transaction=account_balance + amount,
                deposit_withdrawal_type=d_w_type,
                transaction_description="입금",
            )

        if d_w_type == "withdrawal":
            transaction = TransactionHistory.objects.create(
                account_id=account_id,
                transaction_amount=amount,
                transaction_type=transaction_type,
                balance_after_transaction=account_balance - amount,
                deposit_withdrawal_type=d_w_type,
                transaction_description="출금",
            )

        transaction_serializer = TransactionHistorySerializer(transaction)
        return Response(transaction_serializer.data, status=status.HTTP_200_OK)


class AccountDetailAPIView(APIView):

    def get(self, request, id):
        token = request.COOKIES.get("access_token")
        serializer = GetJwtSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")

        try:
            account = Account.objects.get(user_id=user.id, id=id)
        except Account.DoesNotExist:
            return Response({"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        account_serializer = AccountSerializer(account)
        transactions = TransactionHistory.objects.filter(account_id=account.id)
        transaction_serializer = TransactionHistorySerializer(transactions, many=True)

        response_data = {"account": account_serializer.data, "transactions": transaction_serializer.data}

        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        token = request.COOKIES.get("access_token")
        serializer = GetJwtSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")

        try:
            account = Account.objects.get(user_id=user.id, id=id)
        except Account.DoesNotExist:
            return Response({"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        account.delete()
        return Response({"detail": "Account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
