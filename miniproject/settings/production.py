import os

DEBUG = False

ALLOWED_HOSTS: list[str] = ["3.34.200.181"]

ROOT_URLCONF = "miniproject.urls.production_urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": "oz-mini-project-db1.cjcg00o4mbuu.ap-northeast-2.rds.amazonaws.com",
        "PORT": "5432",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")