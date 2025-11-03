from .base import *
import os
from pathlib import Path

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY", "cambia_esta_clave_unica_y_larga")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "jumsag.pythonanywhere.com").split(",")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

LOGGING["root"]["level"] = "WARNING"
