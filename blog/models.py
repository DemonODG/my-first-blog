from django.db import models

# Create your models here.

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    text_short=models.TextField(blank=True, verbose_name='Краткое содержание')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def not_approved_comments(self):
        return self.comments.filter(approved_comment = False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200, verbose_name='Автор')
    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

