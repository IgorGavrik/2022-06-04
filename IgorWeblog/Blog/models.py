from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Task(models.Model):
    # objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Текст')
    created_dt = models.DateTimeField('Дата', auto_now=True)
    publish = models.DateTimeField('Публикация', default=timezone.now)
    slug = models.SlugField('Ссылка', max_length=250, unique=True, null=False, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.publish)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


# class Article(models.Model):
#     title = models.CharField('Название', max_length=50)
#     task = models.TextField('Текст')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(args, kwargs)
#         self.slug = None
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('article_detail', args=self.slug)
