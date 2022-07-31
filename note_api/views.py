from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from note.models import Note, User
from . import serializers, permissions


class NoteAPIView(ListCreateAPIView):
    """ Создание и просмотр постов """
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, permissions.OnlyAuthorEditNote]
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer


class UsersAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer


class UsersDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
