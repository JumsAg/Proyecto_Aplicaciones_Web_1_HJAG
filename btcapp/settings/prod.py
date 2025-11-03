from .base import *
DEBUG = False
ALLOWED_HOSTS = ["localhost"]  # en Fase 5 pondrás tu dominio real
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
