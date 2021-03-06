from __future__ import unicode_literals

import os
import platform
import sys

from django_jinja.builtins import DEFAULT_EXTENSIONS
from social_core.pipeline import DEFAULT_AUTH_PIPELINE

if platform.python_implementation() == 'PyPy':
    from psycopg2cffi import compat  # pylint: disable=import-error
    compat.register()


# The name of this site.  Used for branding in the online admin area.

SITE_NAME = 'Example Project'

SITE_DOMAIN = 'example.com'

PREPEND_WWW = True

ALLOWED_HOSTS = [
    SITE_DOMAIN,
    'www.{}'.format(SITE_DOMAIN),
    'www.example.onespace.media',
]

SUIT_CONFIG = {
    'ADMIN_NAME': SITE_NAME,
    'MENU_EXCLUDE': ['default'],
}

# Database settings.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_project',
        'USER': 'example_project',
    }
}


# Absolute path to the directory where all uploaded media files are stored.

MEDIA_ROOT = '/var/www/example_project_media'

MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0o644


# Absolute path to the directory where static files will be collected.

STATIC_ROOT = '/var/www/example_project_static'

STATIC_URL = '/static/'

NODE_MODULES_ROOT = '/var/www/example_project_static'

NODE_MODULES_URL = '/static/'


# Email settings.

EMAIL_HOST = 'smtp.mandrillapp.com'

EMAIL_HOST_USER = 'developers@onespacemedia.com'

EMAIL_HOST_PASSWORD = ''

EMAIL_PORT = 587

EMAIL_USE_TLS = True

SERVER_EMAIL = '{name} <notifications@{domain}>'.format(
    name=SITE_NAME,
    domain=SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = (
    ('Onespacemedia Errors', 'errors@onespacemedia.com'),
)

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False


# Locale settings.

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Auto-discovery of project location.

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BASE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))


# A list of additional installed applications.

INSTALLED_APPS = [

    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'flexible_images',
    'sorl.thumbnail',
    'compressor',

    'django_jinja',
    'django_lazy_image',

    'cms',

    'reversion',
    'historylinks',
    'watson',

    'cms.apps.pages',
    'cms.apps.links',
    'cms.apps.media',
    # Needs to be before `apps.site` so that unregistering social auth models
    # in site/admin.py works.
    'social_django',

    # 'example_project.apps.careers',
    'example_project.apps.components',
    # 'example_project.apps.events',
    # 'example_project.apps.faqs',
    'example_project.apps.news',
    # 'example_project.apps.partners',
    # 'example_project.apps.people',
    'example_project.apps.redirects',
    'example_project.apps.sections',
    'example_project.apps.settings',
    'example_project.apps.site',

    'suit',
    'django.contrib.admin',

    'server_management',
    'django_extensions',
    'cachalot',
    'webpack_loader',
]

# Additional static file locations.

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'assets'),  # For webpack_loader
    os.path.join(SITE_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/',
        'STATS_FILE': os.path.join(BASE_ROOT, 'webpack-stats.json')
    }
}

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
]

COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

THUMBNAIL_PRESERVE_FORMAT = True

# Dispatch settings.

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cms.middleware.LocalisationMiddleware',
    'example_project.apps.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'watson.middleware.SearchContextMiddleware',
    'historylinks.middleware.HistoryLinkFallbackMiddleware',
    'cms.middleware.PublicationMiddleware',
    'cms.apps.pages.middleware.PageMiddleware',
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.Argon2PasswordHasher',
)


ROOT_URLCONF = 'example_project.urls'

WSGI_APPLICATION = 'example_project.wsgi.application'

PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    '^admin/.*',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SITE_ID = 1

# Absolute path to the directory where templates are stored.

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [
            os.path.join(SITE_ROOT, 'assets/svg'),
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.html',
            'match_regex': r'^(?!admin/|reversion/|registration/|sitemap\.xml|debug_toolbar/).*',
            'app_dirname': 'templates',
            'newstyle_gettext': True,
            'extensions': DEFAULT_EXTENSIONS + [
                'webpack_loader.contrib.jinja2ext.WebpackExtension',
                'compressor.contrib.jinja2ext.CompressorExtension',
                'example_project.apps.site.extensions.DjangoNow',
            ],
            'bytecode_cache': {
                'name': 'default',
                'backend': 'django_jinja.cache.BytecodeCache',
                'enabled': False,
            },
            'autoescape': True,
            'auto_reload': False,
            'translation_engine': 'django.utils.translation',
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'cms.context_processors.settings',
                'cms.apps.pages.context_processors.pages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ]
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'cms.context_processors.settings',
                'cms.apps.pages.context_processors.pages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ]
        }
    }
]


# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = 'example_project'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# A secret key used for cryptographic algorithms.

SECRET_KEY = 'a/6rqaaD2QDuokrxbke4f38go6qOSK3rEFqO3FRxsBNTnhoPXJlgjL7a7c+O97zdGo4='
X_FRAME_OPTIONS = 'SAMEORIGIN'

WYSIWYG_OPTIONS = {
    # Overall height of the WYSIWYG
    'height': 500,

    # Main plugins to load, this has been stripped to match the toolbar
    # See https://www.tinymce.com/docs/get-started/work-with-plugins/
    'plugins': [
        'advlist autolink link image lists charmap hr anchor pagebreak',
        'wordcount visualblocks visualchars code fullscreen cmsimage hr template',
        'table contextmenu directionality paste textcolor colorpicker textpattern'
    ],

    # Items to display on the 3 toolbar lines
    'toolbar1': 'code | cut copy paste pastetext | undo redo | bullist numlist | link unlink anchor cmsimage | blockquote charmap',
    'toolbar2': 'template styleselect formatselect | bold italic underline hr | alignleft aligncenter alignright | table | removeformat | subscript superscript',
    'toolbar3': '',

    # Display menubar with dropdowns
    'menubar': False,

    # Make toolbar smaller
    'toolbar_items_size': 'small',

    # These come from assets/html and are moved into these file paths by Gulp
    'templates': [
        {
            'title': 'Test',
            'description': 'A test template',
            'url': '/static/build/html/test.html'
        }
    ],

    'block_formats': 'Paragraph=p;Header 2=h2;Header 3=h3;Header 4=h4;Header 5=h5;Header 6=h6;',

    # Custom style formats
    'style_formats': [
        {
            'title': 'Buttons',
            'items': [
                {
                    'title': 'Primary',
                    'selector': 'a',
                    'classes': 'wys-Button-primary'
                },
                {
                    'title': 'Secondary',
                    'selector': 'a',
                    'classes': 'wys-Button-secondary'
                },
            ]
        },
        {
            'title': 'Titles',
            'items': [
                {
                    'title': 'Small',
                    'selector': 'h1,h2,h3,h4,h5,h6',
                    'classes': 'wys-Title-small'
                },
                {
                    'title': 'Medium',
                    'selector': 'h1,h2,h3,h4,h5,h6',
                    'classes': 'wys-Title-medium'
                },
                {
                    'title': 'Large',
                    'selector': 'h1,h2,h3,h4,h5,h6',
                    'classes': 'wys-Title-large'
                },
                {
                    'title': 'Extra large',
                    'selector': 'h1,h2,h3,h4,h5,h6',
                    'classes': 'wys-Title-extraLarge'
                }
            ]
        }
    ],

    # Make all elements valid
    'valid_elements': '*[*]',

    # Disable automatic URL manipulation
    'convert_urls': False,

    # Make TinyMCE past as text by default
    'paste_as_text': True,

    'image_advtab': True,

    # Custom CSS to style the wysiwyg content area
    'content_css': '/static/build/css/wysiwyg.css'
}

NEWS_APPROVAL_SYSTEM = False

GOOGLE_ANALYTICS = ''
ADMIN_ANALYTICS_ID = GOOGLE_ANALYTICS
ADMIN_ANALYTICS_GOOGLE_API_KEY = ''

# You can get your Client ID & Secret here: https://creativesdk.adobe.com/myapps.html
ADOBE_CREATIVE_SDK_ENABLED = False
ADOBE_CREATIVE_SDK_CLIENT_SECRET = ''
ADOBE_CREATIVE_SDK_CLIENT_ID = ''

TINYPNG_API_KEY = ''

# Google Apps authentication.

# SETUP:
# 1. https://console.developers.google.com/project
# 2. "Create project"
# 3. APIs & auth -> Consent screen
# 4. Select email address
# 5. APIs & auth -> APIs
# 6. Enable "Google+ API"
# 7. APIs & auth -> Credentials
# 8. Create new Client ID -> Web application
# 9. Copy Client ID to KEY below.
# 10. Copy Client Secret to SECRET below.
# 11. Edit settings
# 12. Set authorized domain

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_GOOGLE_PLUS_KEY = ''
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = ''

WHITELISTED_DOMAINS = ['onespacemedia.com']
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['first_name', 'last_name']

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/admin/'
SOCIAL_AUTH_PIPELINE = DEFAULT_AUTH_PIPELINE + (
    'cms.pipeline.make_staff',
)

# Typekit
TYPEKIT_USED = True
TYPEKIT_KIT_ID = ''

SILENCED_SYSTEM_CHECKS = []

THUMBNAIL_QUALITY = 60

# GEOIP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../geoip/'))

if 'test' in sys.argv:
    # The CMS tests use test-only models, which won't be loaded if we only load
    # our real migration files, so point to a nonexistent one, which will make
    # the test runner fall back to 'syncdb' behavior.

    # Note: This will not catch a situation where a developer commits model
    # changes without the migration files.

    MIGRATION_MODULES = {}
    for app in INSTALLED_APPS:
        app_name = app.split('.')[-1]
        MIGRATION_MODULES[app_name] = None

    # Remove the localisation middleware
    if 'cms.middleware.LocalisationMiddleware' in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES = tuple(c for c in MIDDLEWARE_CLASSES if c != 'cms.middleware.LocalisationMiddleware')
