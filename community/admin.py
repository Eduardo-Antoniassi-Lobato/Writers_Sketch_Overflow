from django.contrib import admin
from .models import Post, Author, Tag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    autofilled_fields = {'slug': ('title',)}
    summernote_fields = ('content')
