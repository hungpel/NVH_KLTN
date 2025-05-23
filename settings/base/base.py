"""
Django settings for FINAL-INT4050 project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import configparser
import os


ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

config_parser = configparser.ConfigParser()
config_parser.read(
    os.path.join(BASE_DIR, "settings", ".env")
)

# common settings
config_parser.get("system", "DATABASE_URL")
DEBUG = config_parser.getboolean("system", "DEBUG", fallback=False)
SECRET_KEY = config_parser.get(
    "system", "SECRET_KEY", fallback="YOUR_SECRET_KEY"
)
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "urls"
WSGI_APPLICATION = "wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ASGI_APPLICATION = 'app.asgi.application'

