import requests
from django.conf import settings
from django.contrib.auth import login
from django.http import HttpRequest
from django.urls import reverse

from users.models import User

GITLAB_HOST = "https://gitlab.com"


def _get_redirect_uri(request):
    return request.build_absolute_uri(reverse("gitlab-auth-callback"))


def get_authorization_start_url(request: HttpRequest) -> str:
    return (
        f"{GITLAB_HOST}/oauth/authorize/?"
        f"response_type=code&"
        f"client_id={settings.GITLAB_CLIENT_ID}&"
        f"redirect_uri={_get_redirect_uri(request)}"
    )


def get_token(request: HttpRequest, code: str) -> str:
    """Запрашивает токен по коду авторизации"""
    response = requests.post(
        f"{GITLAB_HOST}/oauth/token/",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "client_id": settings.GITLAB_CLIENT_ID,
            "client_secret": settings.GITLAB_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": _get_redirect_uri(request),
        },
    )
    response.raise_for_status()
    response_data = response.json()
    return response_data["access_token"]


def get_profile(token: str) -> dict:
    """Получает профиль"""
    response = requests.get(
        f"{GITLAB_HOST}/api/v4/user/", headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return response.json()


def login_with_gitlab_user_profile(request: HttpRequest, gitlab_user_profile: dict):
    """Авторизует пользователя на нашем сайте по профилю из Gitlab"""
    email = gitlab_user_profile["email"]
    user, _ = User.objects.get_or_create(email=email)
    login(request, user)
