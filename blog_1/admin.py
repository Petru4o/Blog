from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment, Category, Vote


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {
        'slug': ('title',),
    }


admin.site.register(Category)

admin.site.register(Vote)

admin.site.register(Comment, MPTTModelAdmin)