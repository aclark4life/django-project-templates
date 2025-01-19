import django_mongodb_backend
import dj_database_url
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Check environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
POSTGRES_URI = os.getenv("POSTGRES_URI")

# Determine which URI to use
if MONGODB_URI:
    DATABASE_URL = MONGODB_URI
    settings_dict = django_mongodb_backend.parse_uri(os.environ.get("DATABASE_URL"))
elif POSTGRES_URI:
    DATABASE_URL = POSTGRES_URI
    settings_dict = dj_database_url.parse(os.environ.get("DATABASE_URL"))
else:
    raise ValueError("Neither MONGODB_URI nor POSTGRES_URI is set in the environment variables.")

DATABASES = {"default": 
DEBUG = True
DEFAULT_AUTO_FIELD = "django_mongodb_backend.fields.ObjectIdAutoField"
INSTALLED_APPS = [
    "{{ project_name }}.mongo_apps.MongoWagtailFormsAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailRedirectsAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailEmbedsAppConfig",
    "wagtail.sites",
    "{{ project_name }}.mongo_apps.MongoWagtailUsersAppConfig",
    "wagtail.snippets",
    "{{ project_name }}.mongo_apps.MongoWagtailDocsAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailImagesAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailSearchAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailAdminAppConfig",
    "{{ project_name }}.mongo_apps.MongoWagtailAppConfig",
    "modelcluster",
    "{{ project_name }}.mongo_apps.MongoTaggitAppConfig",
    '{{ project_name }}.mongo_apps.MongoAdminConfig',
    '{{ project_name }}.mongo_apps.MongoAuthConfig',
    '{{ project_name }}.mongo_apps.MongoContentTypesConfig',
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "webpack_boilerplate",
    "polls",
    "debug_toolbar",
    "home",
]

MIGRATION_MODULES = {
    "admin": "mongo_migrations.admin",
    "auth": "mongo_migrations.auth",
    "contenttypes": "mongo_migrations.contenttypes",
    "taggit": "mongo_migrations.taggit",
    "wagtaildocs": "mongo_migrations.wagtaildocs",
    "wagtailredirects": "mongo_migrations.wagtailredirects",
    "wagtailimages": "mongo_migrations.wagtailimages",
    "wagtailsearch": "mongo_migrations.wagtailsearch",
    "wagtailadmin": "mongo_migrations.wagtailadmin",
    "wagtailcore": "mongo_migrations.wagtailcore",
    "wagtailforms": "mongo_migrations.wagtailforms",
    "wagtailembeds": "mongo_migrations.wagtailembeds",
    "wagtailusers": "mongo_migrations.wagtailusers",
}
ROOT_URLCONF = "{{ project_name }}.urls"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend", "build")]

WEBPACK_LOADER = {
    "MANIFEST_FILE": os.path.join(BASE_DIR, "frontend", "build", "manifest.json")
}

SECRET_KEY = "{{ secret_key }}"

TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join("{{ project_name }}", "templates")],
    },
]

ALLOWED_HOSTS = ["*"]

STATIC_URL = "static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

WAGTAIL_SITE_NAME = "{{ project_name }}"

INTERNAL_IPS = [
    "127.0.0.1",
]
