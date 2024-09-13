from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TransactionHistoryViewSet

# 라우터 설정
router = DefaultRouter()
router.register(r"", TransactionHistoryViewSet, basename="transaction")

# URL 패턴 설정
urlpatterns = [
    path("", include(router.urls)),
]
