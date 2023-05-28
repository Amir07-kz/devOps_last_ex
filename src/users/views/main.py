from django.shortcuts import render


def main_view(request):
    context = {}
    return render(request, "users/main.html", context)
