DJANGO_APPs = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

SITE_ID = 1

EXTERNAL_APPS = [
    "django_extensions",
    "django_filters",
    "rest_framework",
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "djangocms_blog",
    "filer",
    "easy_thumbnails",
    "taggit",
    "parler",
    "aldryn_apphooks_config",
    "taggit_autosuggest",
    "meta",
    "sortedm2m",
    "djangocms_text_ckeditor",
]

INTERNAL_APPS = ["app"]

INSTALLED_APPS = DJANGO_APPs + EXTERNAL_APPS + INTERNAL_APPS
