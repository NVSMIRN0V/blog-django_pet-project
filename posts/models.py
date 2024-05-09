from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=False)

    class Meta:
        db_table = 'likes'
        