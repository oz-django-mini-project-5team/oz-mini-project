# type: ignore

from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from miniproject.urls.base_urls import urlpatterns as base_urlpatterns

development_urlpatterns = [
    path("api/v1/users/", include("users.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns = base_urlpatterns + development_urlpatterns
