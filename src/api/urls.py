from django.urls import path

from .api import (
    NotesCreateApi,
    FolderCreateApi,
    NotesApi,
    FolderApi,
    NotesUpdateApi,
    FolderUpdateApi,
    NotesDeleteApi,
    FolderDeleteApi,
)
from .views import main_api, notes, folders_ls, notes_in_folder, notes_user

urlpatterns = [
    path("", main_api, name="main_api"),
    # path(r'notes/', NotesAPIView.as_view(), name='notes-list'),
    # path(r'folder/', FolderAPIView.as_view(), name='folder-list'),
    path("notes/", NotesApi.as_view(), name="notes-list"),
    path("folders/", FolderApi.as_view(), name="folder-list"),
    path("notes/create", NotesCreateApi.as_view(), name="create-notes"),
    path("folders/create", FolderCreateApi.as_view(), name="create-folder"),
    path("notes/update/<int:pk>", NotesUpdateApi.as_view(), name="update-notes"),
    path("folders/update/<int:pk>", FolderUpdateApi.as_view(), name="update-folders"),
    path("notes/delete/<int:pk>", NotesDeleteApi.as_view(), name="delete-notes"),
    path("folders/delete/<int:pk>", FolderDeleteApi.as_view(), name="delete-folders"),
    path("notes/<slug:slug>/", notes, name="notes"),
    path("folders_ls/", folders_ls, name="folders_ls"),
    path("notes_in_folder/<str:name>/", notes_in_folder, name="notes_in_folder"),
    path("notes_user/<int:user_id>/", notes_user, name="notes_user"),
]
