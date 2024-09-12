from django.urls import path

from users import views

urlpatterns = [
    path("register/", views.UserRegisterAPIView.as_view(), name="user_register"),
    path("active/", views.ActivateUser.as_view(), name="activate_user"),
]
