from django.urls import path

from users.views.auth import (
    login_view,
    register_view,
    logout_view,
    gitlab_auth_callback,
)
from users.views.main import main_view

urlpatterns = [
    path("", main_view, name="main"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path(
        "login/gitlab_auth_callback/", gitlab_auth_callback, name="gitlab-auth-callback"
    ),
]
