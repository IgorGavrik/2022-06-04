# Generated by Django 4.0.5 on 2022-07-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_task_created_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(default=0, max_length=250),
        ),
    ]
