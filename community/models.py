from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "published"))


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def author_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.author_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=True)


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    excerpt = models.CharField(max_length=180)
    featured_image = CloudinaryField('image', default='placeholder')
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts")
    content = models.TextField(validators=[MinLengthValidator(10)])
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
