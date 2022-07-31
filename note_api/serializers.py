from datetime import datetime

from rest_framework import serializers

from note.models import User, Note


class NoteSerializer(serializers.ModelSerializer):
    """ Сериализация данных для постов """
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Note
        fields = (
            'id', 'title', 'note', 'create_at', 'update_at',
            'author',
        )

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        create_at = datetime.strptime(ret['create_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        update_at = datetime.strptime(ret['update_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # Конвертируем дату в строку в новом формате
        ret['create_at'] = create_at.strftime('%d %B %Y - %H:%M:%S')
        ret['update_at'] = update_at.strftime('%d %B %Y - %H:%M:%S')
        return ret


class UsersSerializer(serializers.ModelSerializer):
    """ Сериализация данных для списка пользователей """
    # posts = serializers.SlugRelatedField(
    #     slug_field='',
    #     many=True,
    # )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
        )


# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ...
#         fields = ('username', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
