from django.shortcuts import render
from datetime import date
from django.views import generic
from .models import Post, Comment, Tag, Likes

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name = 'index.html'
    paginate_by = 7
    


def index_page(request):
    pass


def posts(request):
    pass


def post_item(request):
    pass
