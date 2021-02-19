from django.contrib import admin

from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')

    list_filter = ('status', 'created', 'publish', 'author')

    search_fields = ('body', 'title')

    prepopulated_fields = {'slug': ('title',)}

    date_hierarchy = 'publish'

    ordering = ('status', 'publish')

    raw_id_fields = ('author',)