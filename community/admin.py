from django.contrib import admin
from .models import Post, Author, Tag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'slug', 'status', 'date')
    summernote_fields = ('content')
    search_fields = ['title', 'content']


admin.site.register(Author)
admin.site.register(Tag)
