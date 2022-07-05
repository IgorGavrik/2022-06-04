from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
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


class Comment(models.Model):
    post = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
