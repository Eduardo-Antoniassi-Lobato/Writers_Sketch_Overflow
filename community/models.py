from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def author_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.author_name()


class Tag(models.Model):
    heading = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.heading


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=10000)
    content = RichTextField()
    likes = models.ManyToManyField(User, related_name='question_post')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        return reverse('community:question-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    question = models.ForeignKey(
        Question, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=900)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_success_url(self):
        return reverse('community:question-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
