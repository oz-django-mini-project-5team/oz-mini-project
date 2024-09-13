from django.contrib import admin

from users.models import User


# mypy: ignore-errors
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "phone_number", "is_superuser", "is_active")

    search_fields = ("email", "name", "phone_number")

    list_filter = ("is_superuser", "is_active")

    list_display_links = ("email",)

    readonly_fields = ("is_superuser",)
