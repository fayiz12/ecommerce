""
Django settings for jerseybox project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=xky85-504kx((a43xrrv6qj6d3$j(7yi=m&d#oz5au@dcmfvy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'unfold',
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.import_export",
    "django.contrib.admin",
    # 'jazzmin',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'tailwind',
    'theme',
    'django_countries.fields',
    'dal',
    'dal_select2',
    'chartjs',
    

    #Custom Apps
    
    'users',
    'products',
    'categories',
    'cart',
    'wishlists',
    'order',
    'payment',
    'coupon',
    'dashboard',
]
TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jerseybox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jerseybox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'JERSEYBOX1',
        'USER':'postgres',
        'PASSWORD':'test123',
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)



AUTH_USER_MODEL = "users.UserProfile"

CSRF_TRUSTED_ORIGINS=['http://127.0.0.1:8000/']



MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")




EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER='jerseybox2@gmail.com'
EMAIL_HOST_PASSWORD='erhmijnahulswpws'
DEFAULT_FROM_EMAIL='jerseybox2@gmail.com'


JAZZMIN_DASHBOARD = [
    #...
    {
        'app_label': 'products',
        'models': [
            'Club',
        ],
        'charts': [
            'products.charts.my_model_chart',  # Replace with your actual chart path
        ],
    },
]



JAZZMIN_SETTINGS = {
    "site_title": "Jersey Box",
    "site_header": "jersey_box_logo",
    "site_brand": "Jersey Box",
    "site_icon": None,
    # Add your own branding here
    "site_logo": "adminlogo.png",
    "welcome_sign": "Welcome to the Jersey Box",
    # Copyright on the footer
    "copyright": "Jersey Box",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "jersey box", "url": "home", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],
   }



# UNFOLD = {
#     "SITE_TITLE": 'JERSEY BOX',
#     "SITE_HEADER": 'JERSEY BOX',
#     "SITE_URL": "/",
   
#     "SITE_SYMBOL": "speed",  # symbol from icon set
    
    
   
    
#     "COLORS": {
#         "primary": {
#             "50": "250 245 255",
#             "100": "243 232 255",
#             "200": "233 213 255",
#             "300": "216 180 254",
#             "400": "192 132 252",
#             "500": "168 85 247",
#             "600": "147 51 234",
#             "700": "126 34 206",
#             "800": "107 33 168",
#             "900": "88 28 135",
#         },
#     },
#     "EXTENSIONS": {
#         "modeltranslation": {
#             "flags": {
#                 "en": "🇬🇧",
#                 "fr": "🇫🇷",
#                 "nl": "🇧🇪",
#             },
#         },
#     },
    
# }

# LOGIN_URL = '/login/'


# key_id :rzp_test_44So9Mr9PHVm6s
# key_secret: CWVNkyRT1kGnJJAEJ9szTj5u

RAZORPAY_API_KEY = 'rzp_test_DVyPyTYnbu9GxV'
RAZORPAY_API_SECRET = 'SI6gwZGiTasYn3C33Y4hvUEG'
