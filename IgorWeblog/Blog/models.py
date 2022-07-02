from django.db import models
from django.utils import timezone


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Текст')
    created_dt = models.DateTimeField('Дата', auto_now=True)
    slug = models.SlugField('Ссылка', max_length=250, unique_for_date='publish')
    publish = models.DateTimeField('Публикация', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'