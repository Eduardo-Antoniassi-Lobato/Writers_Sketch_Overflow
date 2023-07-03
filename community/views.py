from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment, Tag


# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name = 'index.html'
    paginate_by = 7


