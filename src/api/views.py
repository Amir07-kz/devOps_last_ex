from django.http import JsonResponse
from rest_framework.decorators import api_view

from .services import get_text_notes, get_folders, get_notes_in_folder, get_notes_user


@api_view(["POST", "GET"])
def main_api(request):
    return JsonResponse({"status": "ok"})


@api_view(["POST", "GET"])
def notes(request, slug: str):
    """
    Выводит текст конкретной заметки по slug-у
    """
    text = get_text_notes(slug)
    return JsonResponse({"text": text}, status=200)


@api_view(["POST", "GET"])
def folders_ls(request):
    """
    Возвращает список папок
    """
    folders_list = get_folders()
    return JsonResponse({"folders_list": folders_list}, status=200)


@api_view(["POST", "GET"])
def notes_in_folder(request, name: str):
    """
    Возвращает список заметок в конкретной папке
    """
    notes_list = get_notes_in_folder(name)
    return JsonResponse({"notes_list": notes_list}, status=200)


@api_view(["POST", "GET"])
def notes_user(request, user_id: int):
    """
    Возвращает список заметок конкретного пользователя
    """
    notes_list = get_notes_user(user_id)
    return JsonResponse({"notes_list": notes_list}, status=200)
