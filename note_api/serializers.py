from datetime import datetime

from rest_framework import serializers

from note import models


class NoteSerializer(serializers.ModelSerializer):
    """ Сериализация данных для постов """
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = models.Note
        fields = (
            'id', 'title', 'note', 'create_at',
            'author',
        )

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        create_at = datetime.strptime(ret['create_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # Конвертируем дату в строку в новом формате
        ret['create_at'] = create_at.strftime('%d %B %Y - %H:%M:%S')
        return ret
