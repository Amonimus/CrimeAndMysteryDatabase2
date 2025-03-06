import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent
SECRET_KEY: str = 'django-insecure-l3t3tqv53g(2*7r0dcpb9^3ik241@nzcjj5-9_cbdmy5u!e#&0'
DEBUG: bool = True
ALLOWED_HOSTS: list[str] = []

# Application definition
INSTALLED_APPS: list[str] = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'work',
	'crime',
	'mystery'
]

MIDDLEWARE: list[str] = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Resolver
WSGI_APPLICATION: str = 'app.wsgi.application'
ROOT_URLCONF: str = 'app.urls'

# Database
DATABASES: dict = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# Password validation
AUTH_PASSWORD_VALIDATORS: list[dict] = [
	# {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
	# {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
	# {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
	# {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE: str = 'en-us'
TIME_ZONE: str = 'UTC'
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS: list[str] = [
	os.path.join(BASE_DIR, "web/static/"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'web/static/media')
MEDIA_URL = '/media/'
TEMPLATES: list[dict] = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'web/templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'builtins': [
				'django.templatetags.static',
				'app.templatetags.has_group',
			]
		},
	},
]
