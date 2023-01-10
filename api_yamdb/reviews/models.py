from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import UniqueConstraint

from .validators import validate_username, validate_year


MIN_TITLE_YEAR = 1730


class BaseReviewAndComment(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class BaseCategoryAndGenre(models.Model):
    name = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', unique=True, max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Обязательное поле. Не более 150 символов. '
                  'Только буквы, цифры и символы @/./+/-/_.',
        error_messages={'unique': 'Данное имя пользователя уже занято!'},
        validators=[UnicodeUsernameValidator, validate_username],
        verbose_name='Имя пользователя'
    )
    bio = models.TextField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    role = models.TextField(
        choices=ROLES,
        default=USER
    )


class Category(BaseCategoryAndGenre):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(BaseCategoryAndGenre):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField('Название произведения', max_length=256)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='title',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='title'
    )

    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_TITLE_YEAR),
            validate_year],
        verbose_name='Год издания',
        help_text=(
            'Год не должен быть больше текущего')
    )
    description = models.TextField(
        'Описание произведения',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(BaseReviewAndComment):
    author = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        verbose_name='Оценка произведения',
        help_text='Укажите оценку от 1 до 10'
    )
    title = models.ForeignKey(
        Title,
        related_name='reviews',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            UniqueConstraint(fields=['title', 'author'],
                             name='unique_review')
        ]


class Comment(BaseReviewAndComment):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='comments',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
