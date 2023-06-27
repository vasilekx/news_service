# news/admin.py

from django.contrib import admin

from .models import Comment, Like, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'news', 'author', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'news', 'user')
