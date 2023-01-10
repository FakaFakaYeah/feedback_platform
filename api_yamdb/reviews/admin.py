from django.contrib import admin

from .models import Category, Genre, Title, User, Review, Comment


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


admin.site.register(Title, TitlesAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
