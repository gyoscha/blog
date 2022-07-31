from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from note.models import Note
from . import serializers


class NoteAPIView(ListCreateAPIView):
    """ Создание и просмотр постов """
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
