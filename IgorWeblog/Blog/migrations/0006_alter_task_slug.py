# Generated by Django 4.0.5 on 2022-07-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_task_created_dt_alter_task_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Ссылка'),
        ),
    ]