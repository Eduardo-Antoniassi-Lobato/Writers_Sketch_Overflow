from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Tag


# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).order_by('-date')
    template_name = 'index.html'
    paginate_by = 7
