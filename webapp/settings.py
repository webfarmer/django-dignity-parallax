import os, sys
from django.utils import importlib

sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'apps'))
SITES_DIR = os.path.join(os.path.dirname(__file__), 'sites')
sys.path.append(SITES_DIR)

PROJECT_ROOT = os.path.dirname(__file__); PROJECT_DIR = PROJECT_ROOT

PROJECT_NAME = "Tip Of The Tongue Agency"
PROJECT_DOMAIN = "http://www.tottagency.com"

SECRET_KEY = 'cu&w%kic%b8kw9$=u*jj^w!_+oc*s!zun#=-4$oc^e^7lqyrkt'

SITE_DOMAIN = "http://www.tottagency.com"

DEBUG = True
TEMPLATE_DEBUG = True

MIDDLEWARE_CLASSES = (
    'dynamicsites.middleware.DynamicSitesMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

AUTHENTICATION_BACKENDS = (
    'accounts.backend.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = "/shop/"

# ==============================================================================
# database settings
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'webapp.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# ==============================================================================
# email settings
# ==============================================================================

ADMINS = (
    ('Paul Hoft', 'paul@tensology.com'),
)
MANAGERS = ADMINS

WEBCONTACT_RECIPIENTS = ['paul@tensology.com',]
DEFAULT_FROM_EMAIL = 'info@tensology.com'
SERVER_EMAIL = 'admin@tensology.com'

TEST_EMAIL_DIR = os.path.join(os.path.dirname(__file__), 'tmp', 'test_emails')

MAIL_WRITE_TO_HDD = False

EMAIL_TEST_MODE = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_SYSTEM_SENDER = 'Tip of the Tongue Agency <support@tottagency.com>'

LOGIN_URL = "/login/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
LOCKED_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_locked')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = "/static/"

STATICFILES_DIRS = ()

ADMIN_TOOLS_MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = '/media/'
FILEBROWSER_DIRECTORY = 'upload/'

FILEBROWSER_URL_FILEBROWSER_MEDIA = "/static/filebrowser/"
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser/')

FILEBROWSER_URL_TINYMCE = "/js/tinymce/jscripts/tiny_mce/"
FILEBROWSER_PATH_TINYMCE = STATIC_URL + "tinymce/jscripts/tiny_mce/"

# ==============================================================================
# template handling
# ==============================================================================

TEMPLATE_CONTEXT_PROCESSORS = (
    'dynamicsites.context_processors.current_site',
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.request',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.csrf",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# ==============================================================================
# applications
# ==============================================================================

DJANGO_CONTRIB_APPS = (
    'wpadmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.webdesign',
)

APPS = (
    'accounts',
    'parallax',
    'shop',
    'mails',
    'dynamicsites',
)

THIRD_PARTY_APPS = (
    'easy_thumbnails',
    'debug_toolbar',
    'django_reset',
    'compressor',
    'translatable',
    'south',
)


COMPONENTS = [name for name in os.listdir("%s/components/" % PROJECT_ROOT) if os.path.isdir("%s/components/%s/" % (PROJECT_ROOT,name))]

INSTALLED_APPS = DJANGO_CONTRIB_APPS + THIRD_PARTY_APPS + tuple(APPS) + tuple(COMPONENTS)

TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates'),)

for app in APPS:
    if os.path.isdir(os.path.join(PROJECT_DIR, app, 'templates')):
        TEMPLATE_DIRS += (os.path.join(PROJECT_DIR, app, 'templates'),)

    if os.path.isdir(os.path.join(PROJECT_DIR, app, 'templates/partials')):
        TEMPLATE_DIRS += (os.path.join(PROJECT_DIR, app, 'templates/partials'),)

    if os.path.isdir(os.path.join(PROJECT_DIR, app, 'templates/text')):
        TEMPLATE_DIRS += (os.path.join(PROJECT_DIR, app, 'templates/text'),)

for app in APPS:
    try:
        importlib.import_module("apps.%s.settings" % app)
    except:
        pass

#======================================================================
# TINYMCE Editor Settings
# ==============================================================================

TINYMCE_JS_URL = '/js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    "mode" : "textareas",
    "skin" : "cirkuit",
    "theme" : "advanced",
    "height": 450,
    "width": 900,
    "plugins" : "spellchecker,safari,pagebreak,style,layer,save,advlink,advlist,iespell,inlinepopups,insertdatetime,contextmenu,paste,directionality,noneditable,nonbreaking,xhtmlxtras,template",
    "theme_advanced_buttons1": "bold,italic,strikethrough,|,bullist,numlist,blockquote,|,justifyleft,justifycenter,justifyright,|,link,unlink,|,spellchecker,fullscreen, code",
    "theme_advanced_buttons2": "formatselect,underline,justifyfull,forecolor,|,pastetext,pasteword,removeformat,|,image,charmap,|,outdent,indent,|,undo,redo, help",
    "theme_advanced_buttons3": "",
    "theme_advanced_buttons4": "",
    "theme_advanced_toolbar_location" : "top",
    "theme_advanced_toolbar_align" : "left",
    "theme_advanced_statusbar_location" : "bottom",
    "file_browser_callback" : "CustomFileBrowser",
    "theme_advanced_resizing" : True,
    "convert_urls" : False,
}


ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False
USE_L10N = False
USE_TZ = False
SITE_ID = 1


WPADMIN = {
    'admin': {
        'title': 'TOTTAgency Admin',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/ectoplasm.css',
    }
}


# ==============================================================================
#  overrides settings
# ==============================================================================
try:
    from settings_local import *
except ImportError:
    pass

try:
    from settings_sites import *
except ImportError:
    pass
