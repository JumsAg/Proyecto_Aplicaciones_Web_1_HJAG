from .base import *
import os

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY", "inseguro-dev")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# Base de datos dev: SQLite (simple y suficiente para la Fase 3)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static (por si corres collectstatic luego)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

from .base import *

DEBUG = True

ROOT_URLCONF = "btcsite.urls"
WSGI_APPLICATION = "btcsite.wsgi.application"
ASGI_APPLICATION = "btcsite.asgi.application"
