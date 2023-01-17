from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Comment, Genre, Review, Title, User


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'year',)
    list_editable = ('category', 'year')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'author', 'score', 'pub_date')
    list_editable = ('score',)
    search_fields = ('author',)
    list_filter = ('score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date')
    search_fields = ('author',)
    list_filter = ('author', 'pub_date', 'review')


class CustomUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates',
         {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(Title, TitlesAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(User, CustomUser)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
