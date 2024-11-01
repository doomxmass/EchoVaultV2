from env.SecretKeys import AppSecretKey

ALLAUTH_TEMPLATES = ['django.template.context_processors.request',]

ALLAUTH_AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ALLUTH_INSTALLED_APPS = [
    #- allauth -#
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
]


ALLAUTH_MIDDLEWARE = [
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ALLAUTH_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': AppSecretKey.GITHUB_CLIENT_ID,
            'secret': AppSecretKey.GITHUB_SECRET_KEY
        }
    }
}