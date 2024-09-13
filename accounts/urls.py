from typing import List

from django.urls import path
from django.urls.resolvers import URLPattern

from accounts.views import AccountViewSet

account_list = AccountViewSet.as_view({"get": "list", "post": "create"})

account_detail = AccountViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})

urlpatterns: List[URLPattern] = [
    path("create/", account_list, name="account-create"),
    path("", account_list, name="account-list"),
    path("<int:pk>/", account_detail, name="account-detail"),
    path("<int:pk>/update/", account_detail, name="account-update"),
    path("<int:pk>/delete/", account_detail, name="account-delete"),
]
