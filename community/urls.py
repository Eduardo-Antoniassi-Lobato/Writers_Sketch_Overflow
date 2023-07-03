from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostItem.as_view(), name="post_item"),
]
