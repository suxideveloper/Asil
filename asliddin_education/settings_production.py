"""
Production settings for asliddin_education project.
"""

from .settings import *
import os

# Ensure Jazzmin is properly configured for production
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'education',
]

# Jazzmin Configuration for Production
JAZZMIN_SETTINGS = {
    "site_title": "Asliddin Kurbanov Admin",
    "site_header": "Asliddin Kurbanov",
    "site_brand": "Education Center",
    "welcome_sign": "Asliddin Kurbanov Education Center Admin Panel",
    "copyright": "Asliddin Kurbanov Education Center",
    "search_model": ["education.Teacher", "education.Student", "education.Course"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Website", "url": "/", "new_window": True},
        {"model": "education.Teacher"},
        {"app": "education"},
    ],
    "usermenu_links": [
        {"name": "Website", "url": "/", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["education", "auth"],
    "custom_links": {
        "education": [{
            "name": "View Website",
            "url": "/",
            "icon": "fas fa-external-link-alt",
            "new_window": True,
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "education.Teacher": "fas fa-chalkboard-teacher",
        "education.Student": "fas fa-user-graduate",
        "education.Course": "fas fa-book",
        "education.GraduatedStudent": "fas fa-graduation-cap",
        "education.Achievement": "fas fa-trophy",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Allowed hosts for production
ALLOWED_HOSTS = ['*', 'web-production-37b0.up.railway.app', '.railway.app', '.up.railway.app']

# CSRF settings for Railway
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-37b0.up.railway.app',
    'https://*.railway.app',
    'https://*.up.railway.app',
]

# Database configuration for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files configuration for production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files configuration
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Session settings
SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
CSRF_COOKIE_SECURE = False     # Set to True if using HTTPS

# Email configuration (optional)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
