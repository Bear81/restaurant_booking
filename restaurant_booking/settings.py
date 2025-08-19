"""
Django settings for restaurant_booking.

Django 4.2.x
- Local dev uses SQLite by default.
- Production config (secrets, DB, DEBUG) comes from environment variables.
"""

from pathlib import Path
import os
import sys

# Allow local env vars via env.py without touching Heroku
if os.path.isfile("env.py"):
    import env  # noqa: F401

import dj_database_url

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def env_bool(name: str, default: str = "0") -> bool:
    """Small helper: read booleans from env vars."""
    return os.environ.get(name, default).strip().lower() in {"1", "true", "yes", "on"}


# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
DEFAULT_SQLITE_URL = f"sqlite:///{BASE_DIR / 'db.sqlite3'}"


# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------
# NOTE: SECRET_KEY must be set in production (Heroku Config Vars).
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-insecure-key")  # OK for local only

# Default ON locally; override on Heroku with DEBUG=0
DEBUG = env_bool("DEBUG", "1")

# Comma‑separated list in env; sensible defaults for local + Heroku
ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost,.herokuapp.com"
    ).split(",")
    if h.strip()
]

# CSRF: trust the same hosts over HTTPS (Heroku)
CSRF_TRUSTED_ORIGINS = [
    *(f"https://{h.lstrip('.')}" for h in ALLOWED_HOSTS if "herokuapp.com" in h),
    "https://*.herokuapp.com",
]


# -------------------------------------------------------------------
# Applications
# -------------------------------------------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third‑party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary_storage",
    "cloudinary",
    "django_summernote",

    # Project apps
    "bookings",
    "website",
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Admin login by username
    "django.contrib.auth.backends.ModelBackend",
    # Allauth
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Allauth basics (kept minimal; email verification not required here)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

# Redirects
LOGIN_REDIRECT_URL = "booking_list"   # after login → My Bookings
ACCOUNT_LOGOUT_REDIRECT_URL = "home"  # after logout → Home


# -------------------------------------------------------------------
# Middleware / URLConf / WSGI
# -------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "restaurant_booking.urls"
WSGI_APPLICATION = "restaurant_booking.wsgi.application"


# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(TEMPLATES_DIR),                   # root templates (e.g., account/)
            str(BASE_DIR / "website" / "templates"),  # website/base.html etc.
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # allauth needs this
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# -------------------------------------------------------------------
# Database
# - SQLite for local dev
# - dj-database-url for production (Postgres), SSL when DATABASE_URL is present
# -------------------------------------------------------------------
DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL or DEFAULT_SQLITE_URL,
        conn_max_age=600,
        ssl_require=bool(DATABASE_URL),
    )
}


# -------------------------------------------------------------------
# Password validation
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -------------------------------------------------------------------
# I18N / TZ
# -------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# Static & Media
# - WhiteNoise serves STATIC_ROOT in production
# - Cloudinary for media if credentials provided (or USE_CLOUDINARY=1)
# -------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Recommended WhiteNoise storage (hashed filenames)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Cloudinary only if configured
_cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME")
_api_key = os.environ.get("CLOUDINARY_API_KEY")
_api_secret = os.environ.get("CLOUDINARY_API_SECRET")
USE_CLOUDINARY = env_bool("USE_CLOUDINARY", "0") or all([_cloud_name, _api_key, _api_secret])

if USE_CLOUDINARY:
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": _cloud_name,
        "API_KEY": _api_key,
        "API_SECRET": _api_secret,
    }
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# -------------------------------------------------------------------
# Defaults
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
