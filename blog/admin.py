from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')

