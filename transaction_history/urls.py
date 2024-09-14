from typing import List

from django.urls import path
from django.urls.resolvers import URLPattern

from transaction_history.views import TransactionHistoryViewSet

transaction_list = TransactionHistoryViewSet.as_view({"get": "list", "post": "create"})

transaction_detail = TransactionHistoryViewSet.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns: List[URLPattern] = [
    path("create/", transaction_list, name="transaction-create"),
    path("", transaction_list, name="transaction-list"),
    path("<int:pk>/", transaction_detail, name="transaction-detail"),
    path("<int:pk>/delete/", transaction_detail, name="transaction-delete"),
]
