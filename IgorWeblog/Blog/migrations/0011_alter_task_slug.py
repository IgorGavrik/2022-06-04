# Generated by Django 4.0.5 on 2022-07-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_alter_task_options_alter_task_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=250, verbose_name='Ссылка'),
        ),
    ]
