from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm
from users.services import register_user
from users.gitlab import (
    get_authorization_start_url,
    get_token,
    get_profile,
    login_with_gitlab_user_profile,
)


def gitlab_auth_callback(request):
    code = request.GET.get("code")
    token = get_token(request, code)
    profile = get_profile(token)
    login_with_gitlab_user_profile(request, profile)
    return redirect("repo_analysis")


def register_view(request):
    context = {"form": RegistrationForm()}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        context["form"] = form
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            register_user(email, password)
            context["message"] = "Регистрация прошла успешно"
    return render(request, "users/register.html", context)


def login_view(request):
    form = LoginForm()
    context = {"form": form, "gitlab_auth_link": get_authorization_start_url(request)}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is None:
                form.add_error(None, "Email или пароль неверные")
                context["form"] = form
            else:
                login(request, user)
                next_url = request.POST.get("next")
                if next_url != "":
                    return redirect(next_url)
                return redirect("main")
    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("main")
