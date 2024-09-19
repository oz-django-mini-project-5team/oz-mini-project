from django.urls import path, include

from miniproject.urls.base_urls import urlpatterns as base_urlpatterns

production_urlpatterns: list[str] = [
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
]

urlpatterns = base_urlpatterns + production_urlpatterns
