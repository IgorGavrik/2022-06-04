from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    created_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'