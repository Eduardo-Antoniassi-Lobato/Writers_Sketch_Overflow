from django.contrib import admin
from .models import Question, Author, Tag, Comment

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Tag)
