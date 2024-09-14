# type: ignore


from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.AccountAPIView.as_view(), name="accounts"),
    path("<int:id>", views.AccountDetailAPIView.as_view(), name="account_delete"),
    path("create", views.AccountCreateAPIView.as_view(), name="account_create"),
    path("deposit-withdrawal", views.AccountUpdateAPIView.as_view(), name="account_deposit_withdrawal"),
]
