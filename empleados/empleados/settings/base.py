from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'


# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local Apps
    'aplicaciones.departamento',
    'aplicaciones.empleado',
    'aplicaciones.producto',
    'aplicaciones.categoria',
    'aplicaciones.carrito',
    'aplicaciones.descuentos',
    'aplicaciones.finanzas',
    'aplicaciones.pedido',
    'aplicaciones.stock',
    'aplicaciones.proveedor',
    'aplicaciones.usuario',
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empleados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'], # Direccion de los templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'aplicaciones.usuario.context_processors.carrito_info',
                'aplicaciones.usuario.context_processors.categorias_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'empleados.wsgi.application'
LANGUAGE_CODE = 'es-ar'

#JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_header": "Administración",
    "site_title": "Administración",
}
JAZZMIN_SETTINGS["show_ui_builder"] = True