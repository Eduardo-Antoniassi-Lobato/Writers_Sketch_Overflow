from django.contrib import admin
from .models import Post, Author, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'status', 'date', 'author', 'tags')
    list_display = ('author', 'date', 'title', 'status')
    summernote_fields = ('content')
    search_fields = ['title', 'content', 'author', 'date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('name', 'post', 'date', 'approved')
    search_fields = ('name', 'post', 'date')
    actions = ['approved_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Author)
admin.site.register(Tag)
