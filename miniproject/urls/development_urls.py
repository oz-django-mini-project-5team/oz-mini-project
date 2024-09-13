from django.urls import URLResolver, include, path

from miniproject.urls.base_urls import urlpatterns as base_urlpatterns

development_urlpatterns: list[URLResolver] = [
    path("api/v1/users/", include("users.urls")),
]

urlpatterns = base_urlpatterns + development_urlpatterns
