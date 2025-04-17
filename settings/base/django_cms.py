THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

META_SITE_PROTOCOL = "https"  # set 'http' for non ssl enabled websites
META_USE_SITES = True

META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True  # django-meta 1.x+
META_USE_SCHEMAORG_PROPERTIES = True  # django-meta 2.x+

PARLER_LANGUAGES = {
    1: (
        {
            "code": "vi",
        },
        {
            "code": "en",
        },
    ),
    "default": {
        "fallbacks": ["vi", "en"],
    },
}
