from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ["*"]  
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECRET_KEY = os.getenv("SECRET_KEY", "pon_aqui_una_clave_larga_y_unica")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "jumsag.pythonanywhere.com").split(",")

