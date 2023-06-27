from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_item,
         name="post-item-page")  # posts/a-single-comment
]
