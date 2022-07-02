from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Текст')
    created_dt = models.DateTimeField('Дата', auto_now=True)
    publish = models.DateTimeField('Публикация', default=timezone.now)
    slug = models.SlugField('Ссылка', max_length=250, unique_for_date='publish')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'