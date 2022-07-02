# Generated by Django 4.0.5 on 2022-07-02 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_alter_task_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Ссылка'),
        ),
    ]