from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User
from reviews.validators import validate_username


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = Title


class TitleCreateSerializer(TitleReadSerializer):
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field='slug',
                                         many=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug',
                                            )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Review
        exclude = ('title',)

    def validate(self, data):
        if self.context['request'].method == 'PATCH':
            return data
        if Review.objects.filter(
            author=self.context['request'].user,
            title=self.context['view'].kwargs['title_id']
        ).exists():
            raise serializers.ValidationError(
                'Вы уже оставили отзыв на данное произведение!'
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей"""
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role',
        )


class RegistrationSerializer(serializers.Serializer):
    """Сериализатор регистрации"""
    username = serializers.CharField(
        validators=[UnicodeUsernameValidator, validate_username],
    )
    email = serializers.EmailField()

    def create(self, validated_data):
        try:
            user, status = User.objects.get_or_create(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
            )
            return user
        except IntegrityError:
            raise serializers.ValidationError(
                'Такой пользователь уже зарегистрирован, проверьре ваш email!'
            )


class GetTokenSerializer(serializers.Serializer):
    """Сериализатор получения токена"""
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        if not default_token_generator.check_token(
                get_object_or_404(User, username=data['username']),
                data['confirmation_code']
        ):
            raise serializers.ValidationError(
                'Проверьте правильность confirmation_code '
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        exclude = ('review',)
