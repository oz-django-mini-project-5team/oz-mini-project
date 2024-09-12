from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users import views

urlpatterns = [
    # 회원가입
    path("register/", views.UserRegisterAPIView.as_view(), name="user_register"),
    path("active/", views.ActivateUser.as_view(), name="activate_user"),
    # 토큰
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # 로그인, 로그아웃
    path("login/", views.UserLoginAPIView.as_view(), name="jwt_login"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="jwt_logout"),
]
