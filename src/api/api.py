from rest_framework import generics

from .models import Notes, Folder
from .serializers import NotesSerializer, FolderSerializer


class NotesCreateApi(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class FolderCreateApi(generics.CreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class NotesApi(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class FolderApi(generics.ListAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class NotesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class FolderUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class NotesDeleteApi(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class FolderDeleteApi(generics.DestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
